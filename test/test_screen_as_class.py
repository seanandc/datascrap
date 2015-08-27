import unittest
from requests.exceptions import HTTPError
from datascrap.screens import StockScreen
import os
from mock import patch
import requests
from requests import Response

class ResponseStatus500 (Response):

    def __init__(self):
        self.reason = ""
        self.status_code = 500

class ResponseStatus400 (Response):

    def __init__(self):
        self.reason = ""
        self.status_code = 400

class ResponseStatus200 (Response):

    def __init__(self, yahoo_finance_html_path, test_stock):
        self.reason = ""
        self.status_code = 200

        self.text = open(yahoo_finance_html_path%test_stock,"r").read()


class TestScreenParsingAndOutput(unittest.TestCase):

    def setUp(self):
        self.sp500_test_set = ['a', 'aa',
                               'aapl', 'abbv',
                               'abc', 'abt',
                               'ace', 'aci',
                               'acn', 'adbe',
                               'adi', 'adm',
                               'adp']

        self.yahoo_finance_html_path = os.path.join(
            os.path.split(os.path.abspath(__file__))[0],
            "yahoo_finance_%s_09:00-00:00:00.html"
        )


    def test_request_parse_filter_by_10(self):
        '''
        verify that a certain number filters
        and stock returns the results from out static html
        :return:
        '''

        # ARRANGE
        test_stock = 'aci'
        screen = StockScreen(10)
        yahoo_finance_html = open(self.yahoo_finance_html_path%test_stock,"r").read()
        expected_screen_output = "price to book ratio: aci, 0.05\nPEG ration: aci -0.01\n"

        # ACT
        screen_output = screen._parse(test_stock,yahoo_finance_html)
        print screen_output

        # ASSERT
        self.assertEqual(expected_screen_output,screen_output)

    def test_screen_parse_filter_by_1(self):
        '''
        verify that a certain number filters
        and stock returns the results from out static html
        :return:
        '''

        # ARRANGE
        test_stock = 'aci'
        screen = StockScreen(1)
        yahoo_finance_html = open(self.yahoo_finance_html_path%test_stock,"r").read()
        expected_screen_output = "price to book ratio: aci, 0.05\nPEG ration: aci -0.01\n"

        # ACT
        screen_output = screen._parse(test_stock,yahoo_finance_html)
        print screen_output

        # ASSERT
        self.assertEqual(expected_screen_output,screen_output)

    def test_screen_parse_filter_by_5(self):
        '''
        verify that a certain number filters
        and stock returns the results from out static html
        :return:
        '''

        # ARRANGE
        test_stock = 'aci'
        screen = StockScreen(5)
        yahoo_finance_html = open(self.yahoo_finance_html_path%test_stock,"r").read()
        expected_screen_output = "price to book ratio: aci, 0.05\nPEG ration: aci -0.01\n"

        # ACT
        screen_output = screen._parse(test_stock,yahoo_finance_html)
        print screen_output

        # ASSERT
        self.assertEqual(expected_screen_output,screen_output)

    def test_screen_parse_underfilter_by_3_(self):
        '''
        verify that a certain number does not filter
        correctly when our target is over the filter
        '''

        # ARRANGE
        test_stock = 'a'
        screen = StockScreen(3.0)
        yahoo_finance_html = open(self.yahoo_finance_html_path%test_stock,"r").read()

        # ACT
        screen_output = screen._parse(test_stock,yahoo_finance_html)

        # ASSERT
        self.assertEqual(screen_output, "")

    def test_screen_parse_filter_by_100_all_test_sps(self):
        '''
        pick a number filter that is really big
        and make sure that all our test indexes
        return a value from their respective
        html files that is not an empty string
        :return:
        '''

        # ARRANGE
        screen = StockScreen(100)
        for test_stock in self.sp500_test_set:
            yahoo_finance_html = open(self.yahoo_finance_html_path%test_stock,"r").read()

            # ACT
            screen_output = screen._parse(test_stock,yahoo_finance_html)

            # ASSERT
            self.assertTrue(screen_output)


    @patch.object(requests, "get")
    def test_yahoo_keystats_fail500(self, mockget):
        mockget.return_value = ResponseStatus500()
        screen = StockScreen(100)
        test = False
        try:
            screen.yahooKeyStats('aa')

        except HTTPError:
            test = True

        self.assertEqual(test, True)
        #self.assertRaises(HTTPError, screen.yahooKeyStats, *('aa',))


    @patch.object(requests, "get")
    def test_yahoo_keystats_fail400(self, mockget):
        mockget.return_value = ResponseStatus400()
        screen = StockScreen(100)
        self.assertRaises(HTTPError, screen.yahooKeyStats, *('aa',))

    @patch.object(requests, "get")
    def test_yahoo_keystats_success200(self, mockget):
        mockget.return_value = ResponseStatus200(self.yahoo_finance_html_path, 'aci')
        screen = StockScreen(100)
        expected_screen_output = "price to book ratio: aci, 0.05\nPEG ration: aci -0.01\n"
        output = screen.yahooKeyStats('aci')
        self.assertEqual(expected_screen_output, output)
        #self.assertRaises(HTTPError, screen.yahooKeyStats, *('aa',))


    @unittest.skip("TODO: need to test for failure with mock")
    def test_screen_failure(self):
        pass

    @unittest.skip("TODO: need to test for index errors using mock")
    def test_screen_index_errors(self):
        pass