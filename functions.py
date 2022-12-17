import requests
from bs4 import BeautifulSoup
from time import sleep
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}


def stroygid():
    url = 'https://stroy-gid.su'
    reaponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(reaponse.text, 'lxml')
    map = soup.find_all('h2', class_='bx_sitemap_li_title')
    category = []

    for i in map:
        link = i.find('a').get('href')
        category.append(link)

    for j in category:
        url = f'https://stroy-gid.su{j}'
        reaponse = requests.get(url, headers=headers)
        soup = BeautifulSoup(reaponse.text, 'lxml')
        pages = soup.find('div', class_='bx-pagination-container')
        if pages != None:
            number = len(pages.find_all('span')) - 2
        else:
            number = 1

        for count in range(1, number):
            url = f'https://stroy-gid.su{j}?PAGEN_1={count}'
            reaponse = requests.get(url, headers=headers)
            soup = BeautifulSoup(reaponse.text, 'lxml')
            data = soup.find_all('div', class_='col-sm-4 product-item-big-card')
            for i in data:
                name = i.find('div', class_="product-item-title").text.strip()
                price = i.find('span', class_="product-item-price-old").text.strip().replace(' руб', '').replace(' ', '')
                yield name, price

def profcom():
    url = 'https://www.profkom64.ru/product/'
    reaponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(reaponse.text, 'lxml')
    map = soup.find_all('a', class_='catalogue__item_title')
    category = []
    number = []
    for i in map:
        link = i.get('href')
        category.append(link)
    for j in category:
        url = f'https://www.profkom64.ru{j}'
        reaponse = requests.get(url, headers=headers)
        soup = BeautifulSoup(reaponse.text, 'lxml')
        pages = soup.find('div', class_='pagination')
        pages_number = len(pages.find_all('a')) - 1
        number.append(abs(pages_number))
    for t in category:
        for count in number:
            url = f'https://www.profkom64.ru{t}?filters=&brand=&price=&p={count}'
            reaponse = requests.get(url, headers=headers)
            soup = BeautifulSoup(reaponse.text, 'lxml')
            data = soup.find_all('div', class_='product')
            for p in data:
                name = p.find('a', class_='product_title').text.strip()
                price = p.find('p', class_='price').text.strip().replace('руб. / шт.', '').replace('руб. / упак.', '').replace('руб. / рулон', '').replace('руб. / пог. м', '').replace('руб. / м2', '').replace('руб. / лист', '')
                yield name, price
