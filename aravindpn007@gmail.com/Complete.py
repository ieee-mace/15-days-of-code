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
        data = file.read()
        url = data.split('|')[0]
        desired_price = data.split('|')[1]
        file.close()
    except:
        file = open(filename, 'w')
        url = input('Enter the url: ')
        desired_price = input('Enter your desired price: ')
        print('\n')
        file.write(url + '|')
        file.write(desired_price)
        file.close()

    # Search 'my user agent' in the browser(to get your user agent) and copy and paste it in the variable
    # in the format {'User-Agent: 'Paste here'}
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '

                                'Chrome/81.0.4044.138 Safari/537.36'}

    try:
        page = requests.get(url, headers=user_agent)
        page_content = Soup(page.content, 'html.parser')
        page.close()
        product_name = page_content.find('span', {'id': 'productTitle'}).text.strip()
        try:
            price = page_content.find('span', {'id': 'priceblock_ourprice'}).text
            value = float(price.replace(',', '')[2:])

            print("Product Name: " + product_name)
            print("Current Price: " + price)
            print('\n')

            try:
                if value <= float(desired_price):
                    print('Price dropped!, click the link below\n')
                    print(url)
                    print('\n')
                    f = open(filename, 'w')
                    f.close()
                    grab_price()
                else:
                    print('Waiting for price to drop....')
                    print('[Want to change the product? Hit Ctrl + C]')
                    print('\n')
            except:
                print('The price you entered is invalid')
                f = open(filename, 'w')
                f.close()
                grab_price()

        except:
            print(product_name)
            print('Oops, this product does not have a price\n')
            f = open(filename, 'w')
            f.close()
            grab_price()

    except:
        print('\nInvalid url\n')
        f = open(filename, 'w')
        f.close()
        grab_price()


while True:
    grab_price()
    try:
        time.sleep(20)
        print('Status update: ')
    except KeyboardInterrupt:
        erase = open('my_text.txt', 'w')
        erase.close()
