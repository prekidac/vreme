import argparse, bs4, requests


class Vreme(object):
    
    def __init__(self):
        self.load_page()

    def load_page(self):
        res_obj = requests.get("http://www.hidmet.gov.rs")
        exit(res_obj.text)
        soup_obj = bs4.BeautifulSoup()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trenutna vreme sa hidmet.gov.rs")
    parser.add_argument("-g", help="svi gradovi")
    parser.parse_args()
    v = Vreme()
