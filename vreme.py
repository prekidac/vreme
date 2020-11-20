#! /usr/bin/env python3

import argparse, bs4, requests
import logging

logging.basicConfig(level=logging.DEBUG, filename="o.log")
link = "http://www.hidmet.gov.rs/latin/prognoza/index.php" 


class Vreme(object):
    
    def __init__(self, city: str = "Novi sad"):
        self.load_page()
        self.parse()
        self.city = city

    def load_page(self) -> None:
        res_obj = requests.get(link)
        self.html = res_obj.text

    def parse(self) -> None:
        soup_obj = bs4.BeautifulSoup(self.html, features="html.parser")
        self.rows = soup_obj.select("tr")
    
    def all_cities(self) -> str:
        cities = []
        for row in self.rows[3:-3]:
            soup_obj = bs4.BeautifulSoup(str(row), features="html.parser")
            city = soup_obj.select("td")
            cities.append(city[0].getText().replace(u"\xa0", u"").replace(" ", "_"))
        return ' '.join(cities)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trenutno vreme sa hidmet.gov.rs")
    parser.add_argument("-c", action="store_true", help="list of all cities")
    parser.add_argument("city", action="store", nargs="?", default="Novi sad")
    args = parser.parse_args()
    v = Vreme(args.city)
    if args.c:
        print(v.all_cities())
    else:
        print(args.city)
