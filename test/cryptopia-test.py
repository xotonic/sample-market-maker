from market_maker.cryptopia.cryptopia import CryptopiaAPI
import pprint 

API_KEY = "b5a55135453344ed8677a15141d43f36"
API_SECRET = "oQNB9eHyRZ/12TlIKjL3bp6XsCOA9lZHAXZP5SvXWUI="

printer = pprint.PrettyPrinter(indent=4)

class CryptopiaTest:

    def __init__(self):
        self.api = CryptopiaAPI(symbol='', key=API_KEY, secret=API_SECRET)
        printer.pprint(self.api.get_market('LUX_BTC'))
        

def main():
    test = CryptopiaTest()


if __name__ == "__main__":
    main()
