# About the Project: Web Scraping Using Python - Track prices of products in Amazon.in

# Objective is to build a Python Script that helps us to track the price of a product that we wish to buy,
# so that we need not check the website all the time to see whether the price has dropped and instead Python will
# take care of it!


from bs4 import BeautifulSoup as Soup
import requests
import time


def grab_price():
    filename = 'my_text.txt'

    try:
        file = open(filename, 'r')
        url = file.read()
        file.close()
    except:
        file = open(filename, 'w')
        url = input('Enter the url: ')
        file.write(url)
        file.close()

    # Search 'my user agent' in the browser(to get your user agent) and copy and paste it in the variable
    # in the format {'User-Agent: 'Paste here'}
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/81.0.4044.138 Safari/537.36'}
    page = requests.get(url, headers=user_agent)

    page_content = Soup(page.content, 'html.parser')
    page.close()

    product_name = page_content.find('span', {'id': 'productTitle'}).text.strip()
    try:
        price = page_content.find('span', {'id': 'priceblock_ourprice'}).text
        value = float(price.replace(',', '')[2:])

        print(product_name)
        print(value)
        print('\n')

        if value <= 10000:
            print('Price dropped!, click the link below\n')
            print(url)
    except:
        print(product_name)
        print('Oops, this product does not have a price')


while True:
    grab_price()
    time.sleep(60 * 60)
