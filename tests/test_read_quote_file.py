import unittest
import os

from quote import interpret_data, download_quotes_by_date
from exceptions import NoQuoteForDateException

class TestReadQuote(unittest.TestCase):
    def test_interpret(self):
        date = '20200102'
        download_quotes_by_date(date)
        quote = interpret_data(date)
        assert quote['code'] == 'VES'