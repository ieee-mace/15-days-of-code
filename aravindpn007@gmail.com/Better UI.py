# About the Project: Web Scraping Using Python - Track prices of products in Amazon.in

# Objective is to build a Python Script that helps us to track the price of a product that we wish to buy,
# so that we need not check the website all the time to see whether the price has dropped and instead Python will
# take care of it!


from bs4 import BeautifulSoup as Soup
import requests
from tkinter import *
import webbrowser


def grab_price():
    filename = 'my_text.txt'
    # add_desiredprice_slot.config(state='readonly')
    # add_url_slot.config(state='readonly')

    try:
        file = open(filename, 'r')
        data = file.read()
        url = data.split('|')[0]
        desired_price = data.split('|')[1]
        file.close()
        add_url_slot.delete(0, END)
        add_desiredprice_slot.delete(0, END)
        add_desiredprice_slot.insert(0, desired_price)
        add_url_slot.insert(0, url)
        add_desiredprice_slot.config(state='readonly')
        add_url_slot.config(state='readonly')

    except:
        file = open(filename, 'w')
        url = add_url_slot.get()
        desired_price = add_desiredprice_slot.get()
        file.write(url + '|')
        file.write(desired_price)
        file.close()
        add_desiredprice_slot.config(state='readonly')
        add_url_slot.config(state='readonly')

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

            global product_name_label
            global product_price_label
            global message_label
            product_name_label.destroy()
            product_name_label = Label(root, text="Product: " + product_name)
            product_name_label.grid(row=3, column=0)
            product_price_label.destroy()
            product_price_label = Label(root, text="Current Price: " + price)
            product_price_label.grid(row=4, column=0)

            try:
                if value <= float(desired_price):
                    message_label.destroy()
                    message_label = Label(root, text='Price dropped!', fg='green')
                    message_label.grid(row=1, column=3)
                    visit_page_button.config(state=NORMAL)
                else:
                    message_label.destroy()
                    message_label = Label(root, text='No price drop')
                    message_label.grid(row=1, column=3)
                    visit_page_button.config(state=NORMAL)
            except:
                message_label.destroy()
                message_label = Label(root, text='Add a valid price', fg='red')
                message_label.grid(row=1, column=3)
                f = open(filename, 'w')
                f.close()
                add_desiredprice_slot.config(state='normal')
                add_url_slot.config(state='normal')

        except:
            product_price_label.destroy()
            product_name_label.destroy()
            product_name_label = Label(root, text="Product: " + product_name)
            product_name_label.grid(row=3, column=0)
            message_label = Label(root, text='No price listed in Amazon', fg='red')
            message_label.grid(row=1, column=3)
            f = open(filename, 'w')
            f.close()
            add_desiredprice_slot.config(state='normal')
            add_url_slot.config(state='normal')

    except:
        message_label.destroy()
        message_label = Label(root, text='Invalid url', fg='red')
        message_label.grid(row=1, column=3)
        f = open(filename, 'w')
        f.close()
        add_desiredprice_slot.config(state='normal')
        add_url_slot.config(state='normal')


def clear_product():
    global product_name_label
    global product_price_label
    global message_label
    file = open('my_text.txt', 'w')
    file.close()
    add_desiredprice_slot.config(state='normal')
    add_url_slot.config(state='normal')
    add_url_slot.delete(0, END)
    add_desiredprice_slot.delete(0, END)
    product_name_label.destroy()
    product_price_label.destroy()
    visit_page_button.config(state=DISABLED)
    message_label.destroy()


def open_page():
    webbrowser.open(add_url_slot.get())


def read_after_app_start():
    read_data = open('my_text.txt', 'r')
    rf = read_data.read()
    try:
        saved_url = rf.split('|')[0]
        saved_desired_price = rf.split('|')[1]
        add_url_slot.insert(0, saved_url)
        add_desiredprice_slot.insert(0, saved_desired_price)
        add_url_slot.config(state='readonly')
        add_desiredprice_slot.config(state='readonly')
    except:
        pass


root = Tk()
root.title('Price Tracker')

product_name_label = Label(root)
product_price_label = Label(root)
message_label = Label(root)

title_label = Label(root, text='DEMO')
title_label.grid(row=0, column=0, columnspan=3)

add_url_slot = Entry(root, width=100, borderwidth=3)
add_url_slot.grid(row=1, column=0)
add_url_slot.insert(0, 'paste url here...')

check_button = Button(root, text='Check', command=grab_price, padx=27)
check_button.grid(row=1, column=2)

add_desiredprice_slot = Entry(root, width=100, borderwidth=3)
add_desiredprice_slot.grid(row=2, column=0)
add_desiredprice_slot.insert(0, 'desired price here...')

remove_button = Button(root, text='Reset', fg='red', command=clear_product, padx=29)
remove_button.grid(row=2, column=2)

visit_page_button = Button(root, text='Visit Page', command=open_page, padx=15, fg='blue')
visit_page_button.grid(row=2, column=3)
visit_page_button.config(state=DISABLED)


def on_entry_click(event):
    if add_url_slot.get() == 'paste url here...':
        add_url_slot.delete(0, "end")  # delete all the text in the entry
        add_url_slot.insert(0, '')  # Insert blank for user input
        add_url_slot.config(fg='black')


def on_focusout(event):
    if add_url_slot.get() == '':
        add_url_slot.insert(0, 'paste url here...')
        add_url_slot.config(fg='grey')


add_url_slot.bind('<FocusIn>', on_entry_click)
add_url_slot.bind('<FocusOut>', on_focusout)
add_url_slot.config(fg='grey')


def on_entry_click_2(event):
    if add_desiredprice_slot.get() == 'desired price here...':
        add_desiredprice_slot.delete(0, "end")  # delete all the text in the entry
        add_desiredprice_slot.insert(0, '')  # Insert blank for user input
        add_desiredprice_slot.config(fg='black')


def on_focusout_2(event):
    if add_desiredprice_slot.get() == '':
        add_desiredprice_slot.insert(0, 'desired price here...')
        add_desiredprice_slot.config(fg='grey')


add_desiredprice_slot.bind('<FocusIn>', on_entry_click_2)
add_desiredprice_slot.bind('<FocusOut>', on_focusout_2)
add_desiredprice_slot.config(fg='grey')
root.mainloop()
