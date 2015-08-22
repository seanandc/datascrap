import unittest
from datascrap.screens import StockScreen
import os


class TestScreenAsFunction(unittest.TestCase):

    def setUp(self):
        self.sp500_test_set = ['a', 'aa',
                               'aapl', 'abbv',
                               'abc', 'abt',
                               'ace', 'aci',
                               'acn', 'adbe',
                               'adi', 'adm',
                               'adp']

        self.yahoo_finance_html_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],"yahoo_finance_output_082215_10:00:00.html")
        self.yahoo_finance_html = open(self.yahoo_finance_html_path,"r").read()


    @unittest.skip("TODO: need to test for failure with mock")
    def test_screen_failure(self):
        pass

    @unittest.skip("TODO: need to test for index errors using mock")
    def test_screen_index_errors(self):
        pass

    def test_request_parse_filter_by_10(self):
        '''
        verify that a certain number filter
        and stock returns the results from out static html
        :return:
        '''

        # ARRANGE
        screen = StockScreen(10)
        expected_screen_output = "price to book ratio: aci, 8.02\nPEG ration: aci 2.43\n"

        # ACT
        screen_output = screen._parse('aci',self.yahoo_finance_html)

        # ASSERT
        self.assertEqual(expected_screen_output,screen_output)



    @unittest.skip("TODO: need more tests around different number filters")
    def test_screen_parse_filter_by_1(self):
        pass

    @unittest.skip("TODO: need more tests around different number filters")
    def test_screen_parse_filter_by_5(self):
        pass

