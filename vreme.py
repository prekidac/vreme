#! /usr/bin/env python3

import argparse, bs4, requests
from colored import fg, attr

link = "http://www.hidmet.gov.rs/latin/osmotreni/index.php" 


class Vreme(object):
    
    def __init__(self, city: str = "Novi_sad"):
        self.load_page()
        self.parse()
        self.all_cities()
        self.cities = city

    def load_page(self) -> None:
        res_obj = requests.get(link)
        self.html = res_obj.text

    def parse(self) -> None:
        soup_obj = bs4.BeautifulSoup(self.html, features="html.parser")
        self.rows = soup_obj.select("tr")
    
    def all_cities(self) -> None:
        self.lst_all_cities = []
        self.lst_all_temps = []
        for row in self.rows[5:-4]:
            soup_obj = bs4.BeautifulSoup(str(row), features="html.parser")
            city = soup_obj.select("td")
            self.lst_all_cities.append(city[0].getText().replace(u"\xa0", u"").replace(" ", "_"))
            try: 
                self.lst_all_temps.append(round(float(city[1].getText().replace(u"\xa0", u"").strip())))
            except:
                self.lst_all_temps.append(round(float(city[2].getText().replace(u"\xa0", u"").strip())))

        return(' '.join(self.lst_all_cities))
    
    def cities_temp_print(self) -> None:
        MAX = 10
        for i in self.cities:
            if len(i) > MAX: MAX = len(i)
        for city in self.cities:
            if city in self.lst_all_cities:
                self.temp = self.lst_all_temps[self.lst_all_cities.index(city)]
                print(f"""{fg(4) + attr(1) + city.ljust(MAX) + attr('reset')} {fg(2) + attr(1) + 
                    str(self.temp) + attr('reset')} {fg(8)}{attr('reset')}""")
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
