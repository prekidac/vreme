import argparse, bs4, requests
import logging

logging.basicConfig(level=logging.DEBUG, filename="o.log")
link = "http://www.hidmet.gov.rs/latin/prognoza/index.php" 


class Vreme(object):
    
    def __init__(self):
        self.load_page()
        self.parse()

    def load_page(self):
        res_obj = requests.get(link)
        self.html = res_obj.text
        logging.debug(self.html)

    def parse(self):
        soup_obj = bs4.BeautifulSoup(self.html, features="html.parser")
        self.rows = soup_obj.select("tr")
        exit(self.rows[0].getText())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trenutna vreme sa hidmet.gov.rs")
    parser.add_argument("-g", help="svi gradovi")
    parser.parse_args()
    v = Vreme()
