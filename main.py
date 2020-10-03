import sys

from input_checker import check_args
from exceptions import NoQuoteForDateException
from quote import get_best_quote_by_date

def print_best_quote_for_date(date, show_code):
    try:
        best_quote = get_best_quote_by_date(date)
        if show_code:
            print(best_quote['code']+', '+best_quote['symbol'] +', ' + best_quote['countries'] + ', %.8f' % best_quote['value'])
        else:
            print(best_quote['symbol'] +', ' + best_quote['countries'] + ', %.8f' % best_quote['value'])
    except NoQuoteForDateException as e:
        print('x')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if(check_args(sys.argv)):
        if(len(sys.argv) > 2):
            print_best_quote_for_date(sys.argv[1], True)
        else:
            print_best_quote_for_date(sys.argv[1], False)
        
