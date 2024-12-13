
from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.cursbnr.ro/")
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

rows = soup.find_all("tr")
for row in rows:
    currency_td = row.find("td", class_="text-center hidden-xs")
    if currency_td:
        value_td = None
        for td in row.find_all("td", class_="text-center"):
            if "hidden-xs" not in td.get("class", []):
                value_td = td
                break
        if value_td:
            print(currency_td.text.strip(), value_td.text.strip())

