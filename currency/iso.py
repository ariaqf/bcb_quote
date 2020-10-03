import requests
import xlrd

def get_country_by_iso():
    '''this function aims to read the currency to country data from official iso 4217 xls files'''
    countries = ''
    try:
        iso = xlrd.open_workbook('iso_file.xls')
        sheet = iso.sheet_by_index(0)
        for rx in range(sheet.nrows):
            if(sheet.cell_value(rowx=rx,colx=2) == code):
                #We can't use a break here since more countries may use this currency
                countries += sheet.cell_value(rowx=rx,colx=0)
    except:
        pass
    return countries

def download_iso_file(current):
    '''this function aims to download official iso 4217 xls files'''
    r = None
    if(current):
         r = requests.get('https://www.currency-iso.org/dam/downloads/lists/list_one.xls')
    else:
        r = requests.get('https://www.currency-iso.org/dam/downloads/lists/list_three.xls')
        
    with open('iso_file.xls', 'wb') as f:
            f.write(r.content)
    
def get_country(code):
    '''this function aims to download and read the currency to country data from official iso 4217 xls files'''
    download_iso_file()
    countries = get_country_by_iso()
    if (countries == ''):
        download_iso_file(False)
        countries = get_country_by_iso()
    return countries