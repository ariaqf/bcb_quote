import sys

from exceptions import NoQuoteForDateException
from quote import get_best_quote_by_date

def print_best_quote_for_date(date):
    try:
        best_quote = get_best_quote_by_date(date)
        print(best_quote['symbol'] +', ' + best_quote['countries'] + ', ' + best_quote['value'])
    except NoQuoteForDateException as e:
        print('x')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if(check_args(sys.argv)):
        print_best_quote_for_date(date)
        

