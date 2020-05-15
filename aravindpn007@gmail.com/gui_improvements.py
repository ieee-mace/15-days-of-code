# About the Project: Web Scraping Using Python - Track prices of products in Amazon.in

# Objective is to build a Python Script that helps us to track the price of a product that we wish to buy,
# so that we need not check the website all the time to see whether the price has dropped and instead Python will
# take care of it!


from bs4 import BeautifulSoup as Soup
import requests
from tkinter import *


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
        url = add_url_slot.get()
        desired_price = add_desiredprice_slot.get()
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

            product_name_label = Label(root, text="Product Name: " + product_name)
            product_name_label.grid(row=3, column=0)
            product_price_label = Label(root, text="Current Price: " + price)
            product_price_label.grid(row=4, column=0)

            try:
                if value <= float(desired_price):
                    price_dropped_label = Label(root, text='Price dropped!, click the link', fg='green')
                    price_dropped_label.grid(row=1, column=3)
                    f = open(filename, 'w')
                    f.close()
                else:
                    price_dropped_label = Label(root, text='Price has not dropped', padx=20)
                    price_dropped_label.grid(row=1, column=3)
            except:
                invalid_price_label = Label(root, text='Add a valid price', fg='red', padx=20)
                invalid_price_label.grid(row=1, column=3)
                f = open(filename, 'w')
                f.close()

        except:
            product_name_label = Label(root, text="Product Name: " + product_name)
            product_name_label.grid(row=3, column=0)
            no_price_product = Label(root, text='Oops, this product does not have a price', fg='red')
            no_price_product.grid(row=1, column=3)
            f = open(filename, 'w')
            f.close()

    except:
        invalid_url = Label(root, text='Invalid url', padx=50, fg='red')
        invalid_url.grid(row=1, column=3)
        f = open(filename, 'w')
        f.close()


def clear_product():
    file = open('my_text.txt', 'w')
    file.close()


root = Tk()

title_label = Label(root, text='DEMO')
title_label.grid(row=0, column=0)

add_url_slot = Entry(root, width=80)
add_url_slot.grid(row=1, column=0)
add_url_slot.insert(0, 'paste url here...')

check_button = Button(root, text='Check', command=grab_price, padx=27)
check_button.grid(row=1, column=2)

add_desiredprice_slot = Entry(root, width=80)
add_desiredprice_slot.grid(row=2, column=0)
add_desiredprice_slot.insert(0, 'desired price here..')

remove_button = Button(root, text='Remove Product', bg='red', fg='white', command=clear_product)
remove_button.grid(row=2, column=2)

root.mainloop()
