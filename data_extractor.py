from bs4 import BeautifulSoup
import requests


class Web_Scrap:

    def __init__(self, url):
        self.url = url
        page = requests.get(url)
        # print(page.text)
        self.soup = BeautifulSoup(page.text, features="html.parser")

    def data(self):
        return self.soup.get_text().splitlines()
        

if __name__ == "__main__":
    cl = Web_Scrap('https://www.flipkart.com/nikon-d7500-dslr-camera-body-18-140-mm-lens/p/itme57c2bb8a03cd?pid=DLLFCKK6GET9EEDC&lid=LSTDLLFCKK6GET9EEDCJAOQAJ&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&fm=organic&iid=b17214b8-1439-41bd-bb3c-30c7b90aa7dd.DLLFCKK6GET9EEDC.SEARCH&ppt=hp&ppn=homepage&ssid=jpepq703m80000001706259212577')
    print(cl.data())
    # from bs4 import BeautifulSoup

    # html = """<p class="qotCJE">
    # <a href="https://ejje.weblio.jp/content/to+pay" title="to payの意味" class="crosslink">to pay</a>
    # <a href="https://ejje.weblio.jp/content/charges" title="chargesの意味" class="crosslink">charges</a>
    # from one's
    # <a href="https://ejje.weblio.jp/content/bank+account" title="bank accountの意味" class="crosslink">bank account</a>
    # </p>"""

    # soup = BeautifulSoup(html)

    # print(soup.text)
    # # to pay
    # # charges
    # # from one's
    # # bank account

    # print(soup.text.replace('\n', ' '))
    # # to pay charges from one's bank account 