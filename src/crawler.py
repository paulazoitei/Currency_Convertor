import requests
from bs4 import BeautifulSoup

def get_rates():
    page_to_scrape = requests.get("https://www.cursbnr.ro/")
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

    valuta_valoare = {'RON': 1.0}
    rows = soup.find_all("tr")
    for row in rows:
        currency_td = row.find("td", class_="text-center hidden-xs")
        if currency_td:
            for td in row.find_all("td", class_="text-center"):
                if "hidden-xs" not in td.get("class", []):
                    valuta_valoare[currency_td.text.strip()] = float(td.text.strip())
                    break
    return valuta_valoare
