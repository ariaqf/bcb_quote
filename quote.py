import requests
from exceptions import NoQuoteForDateException, NoQuotesFoundException

def get_best_quote_by_date(date):
    best_quote = None
    download_quotes_by_date(date)
    best_quote = interpret_data(date)
    if (best_quote['code'] == ''):
        raise NoQuotesFoundException('Please check the downloaded file as it\'s failed to be interpreted')
    
    return best_quote
        
def download_quotes_by_date(date):
    '''the goal of this function is to download the reference data.
    We first must get the correct id for download, the id changes by workdays. 
    so we will consult it instead of calculate it since new holidays would break the system.
    Afterwards we just download the CSV of the right id.'''
    url = 'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim'
    data = {'RadOpcao': 2, 'DATAINI':date[6:8]+'/'+date[4:6]+'/'+date[0:4],'DATAFIM': '', 'ChkMoeda': 61}
    x = requests.post(url, data = data)
    url =  'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVTodasAsMoedas&id='
    try:
        url +=  x.text.split('gerarCSVTodasAsMoedas&amp;id=')[1].split('"><img')[0]
    except Exception as e:
        raise NoQuoteForDateException()
    r = requests.get(url)
    with open(date+'.csv', 'wb') as f:
        f.write(r.content)

def interpret_data(date):
    '''the goal of this function is to interpret the reference data in the CSV file.
    We must search the fourth column of the csv for the currency code and the seventh
    column for the quote on how much of the given coin you can get with one dollar.
    As we're asked for the quote which we can buy the most with dollar we must 
    invert the quote (quote^-1)'''
    
    retr = {'code':'', 'value': None}
    with open(date+'.csv', 'r') as f:
        for line in f:
            columns = line.split(';')
            line_name = columns[3]
            line_quote = 1/float(columns[7].replace(',', '.'))
            if(retr['value'] is None or retr['value'] > line_quote):
                retr['code'] = line_name
                retr['value'] = line_quote
    return retr