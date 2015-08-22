import requests
import bs4

def stockScreen(number):
    '''
    as a nested function

    :param number:
    :return:
    '''

    def yahooKeyStats(stock):
        url = 'http://finance.yahoo.com/q/ks?s='
        res = requests.get(url + stock)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        data = soup.select(".yfnc_tabledata1")
        pbr = data[6].getText()
        peg5 = data[4].getText()

        screenOutput = ""
        if float(pbr) < number:
            screenOutput = "price to book ratio: {}, {}\nPEG ration: {} {}\n".format(stock,pbr,stock,peg5)
        return screenOutput

    return yahooKeyStats


class StockScreen(object):
    '''
    as a class
    '''

    def __init__(self, number):
        self.number= number
        self.pbr_index = 6
        self.peg5_index = 4

    def _parse(self, stock, htmlAsText):
        soup = bs4.BeautifulSoup(htmlAsText, "html.parser")
        data = soup.select(".yfnc_tabledata1")

        screenOutput = ""
        try:
            pbr = data[self.pbr_index].getText()
            peg5 = data[self.peg5_index].getText()

            if float(pbr) < self.number:
                screenOutput = "price to book ratio: {}, {}\nPEG ration: {} {}\n".format(stock,pbr,stock,peg5)
        except IndexError:
            pass # catch and gently move on

        return screenOutput

    def yahooKeyStats(self, stock):
        url = 'http://finance.yahoo.com/q/ks?s='
        res = requests.get(url + stock)

        #
        #  NOTE: this will raise an exception
        #  on a bad request 400 or 500
        #
        res.raise_for_status()
        return self._parse(stock,res.text)


