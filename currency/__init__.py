import pycountry
from fall_back import fallback

def get_metadata(currency_code):
    currency = {'countries': None, 'symbol': ''}
    try:
        currency_data = pycountry.currencies.get(alpha_3=currency_code)
        currency['countries'] = currency_data.country
        currency['symbol'] = currency_data.symbol
    except:
        pass
    # We will use a fallback database in case the library doesn't know the currency.
    if countries == '':
        currency['countries'] = get_country_from_fallback(currency_code)
    if symbol == '':
        currency['symbol'] = get_symbol_from_fallback(currency_code)
        
def get_country_from_fallback(code):
    return fallback[code]['countries']
    
def get_symbol_from_fallback(code):
    return fallback[code]['symbol']
