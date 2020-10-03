import unittest
import os

from quote import download_quotes_by_date
from exceptions import NoQuoteForDateException

class TestDownload(unittest.TestCase):
    def test_invalid_date(self):
        #there are no quotes for January 01 of any year
        date = '20200101'
        try:
            download_quotes_by_date(date)
            assert 1 == 0 #if here it has failed
        except NoQuoteForDateException as e:
            pass
        except Exception as e:
            assert 1 == 0
            
    def test_valid_date(self):
        date = '20200102'
        try:
            download_quotes_by_date(date)
            assert os.path.exists(date+'.csv') and os.path.isfile(date+'.csv')
        except NoQuoteForDateException as e:
            assert 1 == 0 #if here it has failed
        except Exception as e:
            assert 1 == 0
            
        