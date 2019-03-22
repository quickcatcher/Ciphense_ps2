# imporing library for fetching HTML content of webpage
import requests
# For scrapping list items txt and links from raw HTML
from bs4 import BeautifulSoup

# Target URL
url = 'https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population'

page = requests.get(url).content

soup = BeautifulSoup(page, 'html.parser')

tables = soup.find_all('table', attrs={'class': 'wikitable'})

print('Cities with population greater than 5 Lakhs according to data from year 2011')

data = {}
for table in tables:
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        if (len(tds) >= 2):
            population = tds[2].text.replace(',', '')
            population = int(population)
            if population < 500000:
                break

            data[tds[1].text] = population
            print('{}: {}'.format(tds[1].text, population))
            print()

while True:
    city = input('City name: ')

    try:
        print('The population of {} is {}'.format(city, data[city]))
    except:
        print('The city name not available in scrapped data')
