import unittest

from input_checker import  *

class TestInputChecker(unittest.TestCase):
    def test_no_input(self):
        args = []
        assert check_args(args) == False
        
    def test_no_date(self):
        args = ['']
        assert check_args(args) == False
        
    def test_invalid_dates(self):
        args = ['', '12341234']
        assert check_args(args) == False
        args = ['', '1234567']
        assert check_args(args) == False
        args = ['', '123456789']
        assert check_args(args) == False
        args = ['', '202001E0']
        assert check_args(args) == False
        args = ['', '202001E0']
        assert check_args(args) == False
        args = ['', '20500101']
        assert check_args(args) == False
        args = ['', '20200001']
        assert check_args(args) == False
        args = ['', '20101301']
        assert check_args(args) == False
        args = ['', '20100100']
        assert check_args(args) == False
        args = ['', '20100132']
        assert check_args(args) == False
        args = ['', '20100230']
        assert check_args(args) == False
        
    def test_valid_date(self):
        args = ['', '20101030']
        assert check_args(args) == True