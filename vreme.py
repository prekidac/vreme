#! /usr/bin/env python3

import argparse, bs4, requests, copy, logging
from colored import fg, attr

FORMAT="%(asctime)s -- %(levelname)s -- %(message)s -- line: %(lineno)s"
logging.basicConfig(format=FORMAT, level=logging.ERROR)
URL = "http://www.hidmet.gov.rs/latin/osmotreni/index.php" 


class Vreme(object):
    
    def __init__(self, city: str = "Novi_sad"):
        self.load_page()
        self.parse()
        self.all_cities()
        self.cities = city

    def load_page(self) -> None:
        try:
            self.html = requests.get(URL).text
        except:
            logging.error("Nema interneta")
            exit(1)

    def parse(self) -> None:
        soup_obj = bs4.BeautifulSoup(self.html, features="html.parser")
        self.rows = soup_obj.select("tr")
    
    def all_cities(self) -> None:
        self.city_temp = {}
        self.city_temp["all"] = "-"
        for row in self.rows[5:-4]:
            soup_obj = bs4.BeautifulSoup(str(row), features="html.parser")
            city = soup_obj.select("td")
            city_name = city[0].getText().replace(u"\xa0", u"").replace(" ", "_")
            try: 
               city_temp = round(float(city[1].getText().replace(u"\xa0", u"").strip()))
            except:
                try:
                    city_temp = round(float(city[2].getText().replace(u"\xa0", u"").strip()))
                except:
                    city_temp = "-"
            self.city_temp[city_name] = city_temp

        return(' '.join(self.city_temp.keys()))
    
    def cities_temp_print(self) -> None:
        if "all" in copy.copy(self.cities): self.cities = self.city_temp.keys()
        MAX = 10
        for i in self.cities:
            if len(i) > MAX: MAX = len(i)
        for city in self.cities:
            if city in self.city_temp.keys():
                print(f"""{fg(4) + attr(1) + city.ljust(MAX) + attr('reset')} {fg(2) + attr(1) + 
                    str(self.city_temp[city]) + attr('reset')} {fg(8)}{attr('reset')}""")
            else:
                WRONG="--"
                print(f"{fg(2) + attr(1)} {WRONG.center(10)} {attr('reset')} ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trenutno vreme sa hidmet.gov.rs")
    parser.add_argument("-c", action="store_true", help="list of all cities")
    parser.add_argument("city", action="store", nargs="*", default=["Novi_Sad"])
    args = parser.parse_args()
    v = Vreme(args.city)
    if args.c:
        print(v.all_cities())
    else:
        v.cities_temp_print()
