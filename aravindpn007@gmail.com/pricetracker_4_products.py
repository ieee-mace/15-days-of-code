""" About the Project: Web Scraping Using Python - Track prices of products in Amazon.in

Objective is to build a Python Script that helps us to track the price of a product that we wish to buy,
so that we need not check the website all the time to see whether the price has dropped and instead Python will
take care of it! """

from bs4 import BeautifulSoup as Soup
import requests
from tkinter import *
import webbrowser


def grab_price(product_code):
    """ This function will extract name and price of the product, compares with your desired price and gives
    appropriate message """

    # New user?, let python create a pricetracker.txt file as database.
    try:
        file_check = open('pricetracker.txt', 'r')
        file_check.close()
    except:
        create_file = open('pricetracker.txt', 'w')
        default_data = ['.\n', '.\n', '.\n', '.\n', '.']
        create_file.writelines(default_data)
        create_file.close()

    # Update the text file with user input data and assign values for url and desired price.

    filename = 'pricetracker.txt'
    file = open(filename, 'r')
    data = file.readlines()
    url = url_list[product_code - 1].get()
    desired_price = price_list[product_code - 1].get()
    data[product_code - 1] = url + '|' + desired_price + '\n'
    file = open(filename, 'w')
    file.writelines(data)
    file.close()
    price_list[product_code - 1].config(state='readonly')
    url_list[product_code - 1].config(state='readonly')

    # Search 'my user agent' in the browser(to get your user agent) and copy and paste it in the variable
    # in the format {'User-Agent: 'Paste here'}

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '

                                'Chrome/81.0.4044.138 Safari/537.36'}

    # Try to extract data from Amazon.in
    try:
        page = requests.get(url, headers=user_agent)
        page_content = Soup(page.content, 'html.parser')
        page.close()
        product_name = page_content.find('span', {'id': 'productTitle'}).text.strip()

        # Check whether the product has a price
        try:
            price = page_content.find('span', {'id': 'priceblock_ourprice'}).text
            value = float(price.replace(',', '')[2:])

            # Display product name and price
            if product_code - 1 == 0:
                global product_name_label
                global message_label
                product_name_label.destroy()
                product_name_label = Label(root, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                           relief='solid')
                product_name_label.grid(row=3, column=0, pady=5)

            elif product_code - 1 == 1:
                global product_name_label1
                global message_label1
                product_name_label1.destroy()
                product_name_label1 = Label(root, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                            relief='solid')
                product_name_label1.grid(row=7, column=0, pady=5)

            elif product_code - 1 == 2:
                global product_name_label2
                global message_label2
                product_name_label2.destroy()
                product_name_label2 = Label(root, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                            relief='solid')
                product_name_label2.grid(row=11, column=0, pady=5)

            elif product_code - 1 == 3:
                global product_name_label3
                global message_label3
                product_name_label3.destroy()
                product_name_label3 = Label(root, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                            relief='solid')
                product_name_label3.grid(row=15, column=0, pady=5)

            # Display appropriate message
            try:
                if product_code - 1 == 0:
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

                elif product_code - 1 == 1:
                    if value <= float(desired_price):
                        message_label1.destroy()
                        message_label1 = Label(root, text='Price dropped!', fg='green')
                        message_label1.grid(row=5, column=3)
                        visit_page_button1.config(state=NORMAL)
                    else:
                        message_label1.destroy()
                        message_label1 = Label(root, text='No price drop')
                        message_label1.grid(row=5, column=3)
                        visit_page_button1.config(state=NORMAL)

                elif product_code - 1 == 2:
                    if value <= float(desired_price):
                        message_label2.destroy()
                        message_label2 = Label(root, text='Price dropped!', fg='green')
                        message_label2.grid(row=9, column=3)
                        visit_page_button2.config(state=NORMAL)
                    else:
                        message_label2.destroy()
                        message_label2 = Label(root, text='No price drop')
                        message_label2.grid(row=9, column=3)
                        visit_page_button2.config(state=NORMAL)

                elif product_code - 1 == 3:
                    if value <= float(desired_price):
                        message_label3.destroy()
                        message_label3 = Label(root, text='Price dropped!', fg='green')
                        message_label3.grid(row=13, column=3)
                        visit_page_button3.config(state=NORMAL)
                    else:
                        message_label3.destroy()
                        message_label3 = Label(root, text='No price drop')
                        message_label3.grid(row=13, column=3)
                        visit_page_button3.config(state=NORMAL)

            # What if user entered an invalid price?
            except:
                if product_code - 1 == 0:
                    message_label.destroy()
                    message_label = Label(root, text='Add a valid price', fg='red')
                    message_label.grid(row=1, column=3)
                    f = open(filename, 'r')  # Delete the data stored in the text file.
                    d = f.readlines()
                    d[product_code - 1] = '.\n'
                    f = open(filename, 'w')
                    f.writelines(d)
                    f.close()
                    add_desiredprice_slot.config(state='normal')
                    add_url_slot.config(state='normal')

                elif product_code - 1 == 1:
                    message_label1.destroy()
                    message_label1 = Label(root, text='Add a valid price', fg='red')
                    message_label1.grid(row=5, column=3)
                    f = open(filename, 'r')
                    d = f.readlines()
                    d[product_code - 1] = '.\n'
                    f = open(filename, 'w')
                    f.writelines(d)
                    f.close()
                    add_desiredprice_slot1.config(state='normal')
                    add_url_slot1.config(state='normal')

                elif product_code - 1 == 2:
                    message_label2.destroy()
                    message_label2 = Label(root, text='Add a valid price', fg='red')
                    message_label2.grid(row=9, column=3)
                    f = open(filename, 'r')
                    d = f.readlines()
                    d[product_code - 1] = '.\n'
                    f = open(filename, 'w')
                    f.writelines(d)
                    f.close()
                    add_desiredprice_slot2.config(state='normal')
                    add_url_slot2.config(state='normal')

                elif product_code - 1 == 3:
                    message_label3.destroy()
                    message_label3 = Label(root, text='Add a valid price', fg='red')
                    message_label3.grid(row=13, column=3)
                    f = open(filename, 'r')
                    d = f.readlines()
                    d[product_code - 1] = '.\n'
                    f = open(filename, 'w')
                    f.writelines(d)
                    f.close()
                    add_desiredprice_slot3.config(state='normal')
                    add_url_slot3.config(state='normal')

        # Some products in Amazon doesn't have price information.
        except:
            if product_code - 1 == 0:
                product_name_label.destroy()
                product_name_label = Label(root, text="Product: " + product_name, relief='solid')
                product_name_label.grid(row=3, column=0, pady=5)
                message_label = Label(root, text='No price listed in Amazon', fg='red')
                message_label.grid(row=1, column=3)
                f = open(filename, 'r')
                d = f.readlines()
                d[product_code - 1] = '.\n'
                f = open(filename, 'w')
                f.writelines(d)
                f.close()
                add_desiredprice_slot.config(state='normal')
                add_url_slot.config(state='normal')

            elif product_code - 1 == 1:
                product_name_label1.destroy()
                product_name_label1 = Label(root, text="Product: " + product_name, relief='solid')
                product_name_label1.grid(row=7, column=0, pady=5)
                message_label1 = Label(root, text='No price listed in Amazon', fg='red')
                message_label1.grid(row=5, column=3)
                f = open(filename, 'r')
                d = f.readlines()
                d[product_code - 1] = '.\n'
                f = open(filename, 'w')
                f.writelines(d)
                f.close()
                add_desiredprice_slot1.config(state='normal')
                add_url_slot1.config(state='normal')

            elif product_code - 1 == 2:
                product_name_label2.destroy()
                product_name_label2 = Label(root, text="Product: " + product_name, relief='solid')
                product_name_label2.grid(row=11, column=0, pady=5)
                message_label2 = Label(root, text='No price listed in Amazon', fg='red')
                message_label2.grid(row=9, column=3)
                f = open(filename, 'r')
                d = f.readlines()
                d[product_code - 1] = '.\n'
                f = open(filename, 'w')
                f.writelines(d)
                f.close()
                add_desiredprice_slot2.config(state='normal')
                add_url_slot2.config(state='normal')

            elif product_code - 1 == 3:
                product_name_label3.destroy()
                product_name_label3 = Label(root, text="Product: " + product_name, relief='solid')
                product_name_label3.grid(row=15, column=0, pady=5)
                message_label3 = Label(root, text='No price listed in Amazon', fg='red')
                message_label3.grid(row=13, column=3)
                f = open(filename, 'r')
                d = f.readlines()
                d[product_code - 1] = '.\n'
                f = open(filename, 'w')
                f.writelines(d)
                f.close()
                add_desiredprice_slot3.config(state='normal')
                add_url_slot3.config(state='normal')

    # We need to ensure that a non-Amazon url is rejected.
    except:
        if product_code - 1 == 0:
            message_label.destroy()
            message_label = Label(root, text='Invalid url', fg='red')
            message_label.grid(row=1, column=3)
            f = open(filename, 'r')
            d = f.readlines()
            d[product_code - 1] = '.\n'
            f = open(filename, 'w')
            f.writelines(d)
            f.close()
            add_desiredprice_slot.config(state='normal')
            add_url_slot.config(state='normal')

        elif product_code - 1 == 1:
            message_label1.destroy()
            message_label1 = Label(root, text='Invalid url', fg='red')
            message_label1.grid(row=5, column=3)
            f = open(filename, 'r')
            d = f.readlines()
            d[product_code - 1] = '.\n'
            f = open(filename, 'w')
            f.writelines(d)
            f.close()
            add_desiredprice_slot1.config(state='normal')
            add_url_slot1.config(state='normal')

        elif product_code - 1 == 2:
            message_label2.destroy()
            message_label2 = Label(root, text='Invalid url', fg='red')
            message_label2.grid(row=9, column=3)
            f = open(filename, 'r')
            d = f.readlines()
            d[product_code - 1] = '.\n'
            f = open(filename, 'w')
            f.writelines(d)
            f.close()
            add_desiredprice_slot2.config(state='normal')
            add_url_slot2.config(state='normal')

        elif product_code - 1 == 3:
            message_label3.destroy()
            message_label3 = Label(root, text='Invalid url', fg='red')
            message_label3.grid(row=13, column=3)
            f = open(filename, 'r')
            d = f.readlines()
            d[product_code - 1] = '.\n'
            f = open(filename, 'w')
            f.writelines(d)
            f.close()
            add_desiredprice_slot3.config(state='normal')
            add_url_slot3.config(state='normal')


def clear_product(product_code):
    """ Clears / resets all user input fields, clears pricetracker.txt file """

    filename = 'pricetracker.txt'
    if product_code - 1 == 0:
        global product_name_label
        global message_label
        f = open(filename, 'r')
        d = f.readlines()
        d[product_code - 1] = '.\n'
        f = open(filename, 'w')
        f.writelines(d)
        f.close()
        add_desiredprice_slot.config(state='normal')
        add_url_slot.config(state='normal')
        add_url_slot.delete(0, END)
        add_desiredprice_slot.delete(0, END)
        product_name_label.destroy()
        visit_page_button.config(state=DISABLED)
        message_label.destroy()

    elif product_code - 1 == 1:
        global product_name_label1
        global message_label1
        f = open(filename, 'r')
        d = f.readlines()
        d[product_code - 1] = '.\n'
        f = open(filename, 'w')
        f.writelines(d)
        f.close()
        add_desiredprice_slot1.config(state='normal')
        add_url_slot1.config(state='normal')
        add_url_slot1.delete(0, END)
        add_desiredprice_slot1.delete(0, END)
        product_name_label1.destroy()
        visit_page_button1.config(state=DISABLED)
        message_label1.destroy()

    elif product_code - 1 == 2:
        global product_name_label2
        global message_label2
        f = open(filename, 'r')
        d = f.readlines()
        d[product_code - 1] = '.\n'
        f = open(filename, 'w')
        f.writelines(d)
        f.close()
        add_desiredprice_slot2.config(state='normal')
        add_url_slot2.config(state='normal')
        add_url_slot2.delete(0, END)
        add_desiredprice_slot2.delete(0, END)
        product_name_label2.destroy()
        visit_page_button2.config(state=DISABLED)
        message_label2.destroy()

    elif product_code - 1 == 3:
        global product_name_label3
        global message_label3
        f = open(filename, 'r')
        d = f.readlines()
        d[product_code - 1] = '.\n'
        f = open(filename, 'w')
        f.writelines(d)
        f.close()
        add_desiredprice_slot3.config(state='normal')
        add_url_slot3.config(state='normal')
        add_url_slot3.delete(0, END)
        add_desiredprice_slot3.delete(0, END)
        product_name_label3.destroy()
        visit_page_button3.config(state=DISABLED)
        message_label3.destroy()


def open_page(product_code):
    """ Open the web page of the product in your default browser """

    webbrowser.open(url_list[product_code - 1].get())


root = Tk()  # Master window
root.title('Price Tracker')

status = Label(root, text='Developed by Aravind P N', relief=SUNKEN, anchor=E, fg='grey')  # Status bar
status.grid(row=100, column=0, columnspan=4, sticky=E + W)

# Product 1 labels

product_name_label = Label(root)
message_label = Label(root)

# Product 2 labels

product_name_label1 = Label(root)
message_label1 = Label(root)

# Product 3 labels

product_name_label2 = Label(root)
message_label2 = Label(root)

# Product 4 labels

product_name_label3 = Label(root)
message_label3 = Label(root)

# First Product

title_label = Label(root, text='Product 1')
title_label.grid(row=0, column=0, columnspan=3)

add_url_slot = Entry(root, width=100, borderwidth=3)
add_url_slot.grid(row=1, column=0)
add_url_slot.insert(0, 'paste url here...')

check_button = Button(root, text='Check', command=lambda: grab_price(1), padx=27)
check_button.grid(row=1, column=2)

add_desiredprice_slot = Entry(root, width=100, borderwidth=3)
add_desiredprice_slot.grid(row=2, column=0)
add_desiredprice_slot.insert(0, 'desired price here...')

remove_button = Button(root, text='Reset', fg='red', command=lambda: clear_product(1), padx=29)
remove_button.grid(row=2, column=2)

visit_page_button = Button(root, text='Visit Page', command=lambda: open_page(1), padx=15, fg='blue')
visit_page_button.grid(row=2, column=3)
visit_page_button.config(state=DISABLED)

# Second Product

title_label1 = Label(root, text='Product 2')
title_label1.grid(row=4, column=0, columnspan=3)

add_url_slot1 = Entry(root, width=100, borderwidth=3)
add_url_slot1.grid(row=5, column=0)
add_url_slot1.insert(0, 'paste url here...')

check_button1 = Button(root, text='Check', command=lambda: grab_price(2), padx=27)
check_button1.grid(row=5, column=2)

add_desiredprice_slot1 = Entry(root, width=100, borderwidth=3)
add_desiredprice_slot1.grid(row=6, column=0)
add_desiredprice_slot1.insert(0, 'desired price here...')

remove_button1 = Button(root, text='Reset', fg='red', command=lambda: clear_product(2), padx=29)
remove_button1.grid(row=6, column=2)

visit_page_button1 = Button(root, text='Visit Page', command=lambda: open_page(2), padx=15, fg='blue')
visit_page_button1.grid(row=6, column=3)
visit_page_button1.config(state=DISABLED)

# Third Product

title_label2 = Label(root, text='Product 3')
title_label2.grid(row=8, column=0, columnspan=3)

add_url_slot2 = Entry(root, width=100, borderwidth=3)
add_url_slot2.grid(row=9, column=0)
add_url_slot2.insert(0, 'paste url here...')

check_button2 = Button(root, text='Check', command=lambda: grab_price(3), padx=27)
check_button2.grid(row=9, column=2)

add_desiredprice_slot2 = Entry(root, width=100, borderwidth=3)
add_desiredprice_slot2.grid(row=10, column=0)
add_desiredprice_slot2.insert(0, 'desired price here...')

remove_button2 = Button(root, text='Reset', fg='red', command=lambda: clear_product(3), padx=29)
remove_button2.grid(row=10, column=2)

visit_page_button2 = Button(root, text='Visit Page', command=lambda: open_page(3), padx=15, fg='blue')
visit_page_button2.grid(row=10, column=3)
visit_page_button2.config(state=DISABLED)

# Fourth Product

title_label3 = Label(root, text='Product 4')
title_label3.grid(row=12, column=0, columnspan=3)

add_url_slot3 = Entry(root, width=100, borderwidth=3)
add_url_slot3.grid(row=13, column=0)
add_url_slot3.insert(0, 'paste url here...')

check_button3 = Button(root, text='Check', command=lambda: grab_price(4), padx=27)
check_button3.grid(row=13, column=2)

add_desiredprice_slot3 = Entry(root, width=100, borderwidth=3)
add_desiredprice_slot3.grid(row=14, column=0)
add_desiredprice_slot3.insert(0, 'desired price here...')

remove_button3 = Button(root, text='Reset', fg='red', command=lambda: clear_product(4), padx=29)
remove_button3.grid(row=14, column=2)

visit_page_button3 = Button(root, text='Visit Page', command=lambda: open_page(4), padx=15, fg='blue')
visit_page_button3.grid(row=14, column=3)
visit_page_button3.config(state=DISABLED)

# Lists

url_list = [add_url_slot, add_url_slot1, add_url_slot2, add_url_slot3]
price_list = [add_desiredprice_slot, add_desiredprice_slot1, add_desiredprice_slot2, add_desiredprice_slot3]
product_label_list = [product_name_label, product_name_label1, product_name_label2, product_name_label3]
message_label_list = [message_label, message_label1, message_label2, message_label3]


# paste url here... desired price here... should be gone once we click the input field


def on_entry_click_product1(event):
    """ paste url here... disappears when we click the field """

    if add_url_slot.get() == 'paste url here...':
        add_url_slot.delete(0, "end")  # delete all the text in the entry
        add_url_slot.insert(0, '')  # Insert blank for user input
        add_url_slot.config(fg='black')


def on_focusout_product1(event):
    """ paste url here... reappears when we leave the field empty """

    if add_url_slot.get() == '':
        add_url_slot.insert(0, 'paste url here...')
        add_url_slot.config(fg='grey')


def on_entry_click_2_product1(event):
    """ desired price here... disappears when we click the field """

    if add_desiredprice_slot.get() == 'desired price here...':
        add_desiredprice_slot.delete(0, "end")  # delete all the text in the entry
        add_desiredprice_slot.insert(0, '')  # Insert blank for user input
        add_desiredprice_slot.config(fg='black')


def on_focusout_2_product1(event):
    """ desired price here... reappears when leave the field empty """

    if add_desiredprice_slot.get() == '':
        add_desiredprice_slot.insert(0, 'desired price here...')
        add_desiredprice_slot.config(fg='grey')


# bind the above functions to the entry fields

add_url_slot.bind('<FocusIn>', on_entry_click_product1)
add_url_slot.bind('<FocusOut>', on_focusout_product1)
add_url_slot.config(fg='grey')

add_desiredprice_slot.bind('<FocusIn>', on_entry_click_2_product1)
add_desiredprice_slot.bind('<FocusOut>', on_focusout_2_product1)
add_desiredprice_slot.config(fg='grey')


# Similar functions for other products

def on_entry_click_product2(event):
    if add_url_slot1.get() == 'paste url here...':
        add_url_slot1.delete(0, "end")  # delete all the text in the entry
        add_url_slot1.insert(0, '')  # Insert blank for user input
        add_url_slot1.config(fg='black')


def on_focusout_product2(event):
    if add_url_slot1.get() == '':
        add_url_slot1.insert(0, 'paste url here...')
        add_url_slot1.config(fg='grey')


def on_entry_click_2_product2(event):
    if add_desiredprice_slot1.get() == 'desired price here...':
        add_desiredprice_slot1.delete(0, "end")  # delete all the text in the entry
        add_desiredprice_slot1.insert(0, '')  # Insert blank for user input
        add_desiredprice_slot1.config(fg='black')


def on_focusout_2_product2(event):
    if add_desiredprice_slot1.get() == '':
        add_desiredprice_slot1.insert(0, 'desired price here...')
        add_desiredprice_slot1.config(fg='grey')


add_url_slot1.bind('<FocusIn>', on_entry_click_product2)
add_url_slot1.bind('<FocusOut>', on_focusout_product2)
add_url_slot1.config(fg='grey')

add_desiredprice_slot1.bind('<FocusIn>', on_entry_click_2_product2)
add_desiredprice_slot1.bind('<FocusOut>', on_focusout_2_product2)
add_desiredprice_slot1.config(fg='grey')


def on_entry_click_product3(event):
    if add_url_slot2.get() == 'paste url here...':
        add_url_slot2.delete(0, "end")  # delete all the text in the entry
        add_url_slot2.insert(0, '')  # Insert blank for user input
        add_url_slot2.config(fg='black')


def on_focusout_product3(event):
    if add_url_slot2.get() == '':
        add_url_slot2.insert(0, 'paste url here...')
        add_url_slot2.config(fg='grey')


def on_entry_click_2_product3(event):
    if add_desiredprice_slot2.get() == 'desired price here...':
        add_desiredprice_slot2.delete(0, "end")  # delete all the text in the entry
        add_desiredprice_slot2.insert(0, '')  # Insert blank for user input
        add_desiredprice_slot2.config(fg='black')


def on_focusout_2_product3(event):
    if add_desiredprice_slot2.get() == '':
        add_desiredprice_slot2.insert(0, 'desired price here...')
        add_desiredprice_slot2.config(fg='grey')


add_url_slot2.bind('<FocusIn>', on_entry_click_product3)
add_url_slot2.bind('<FocusOut>', on_focusout_product3)
add_url_slot2.config(fg='grey')

add_desiredprice_slot2.bind('<FocusIn>', on_entry_click_2_product3)
add_desiredprice_slot2.bind('<FocusOut>', on_focusout_2_product3)
add_desiredprice_slot2.config(fg='grey')


def on_entry_click_product4(event):
    if add_url_slot3.get() == 'paste url here...':
        add_url_slot3.delete(0, "end")  # delete all the text in the entry
        add_url_slot3.insert(0, '')  # Insert blank for user input
        add_url_slot3.config(fg='black')


def on_focusout_product4(event):
    if add_url_slot3.get() == '':
        add_url_slot3.insert(0, 'paste url here...')
        add_url_slot3.config(fg='grey')


def on_entry_click_2_product4(event):
    if add_desiredprice_slot3.get() == 'desired price here...':
        add_desiredprice_slot3.delete(0, "end")  # delete all the text in the entry
        add_desiredprice_slot3.insert(0, '')  # Insert blank for user input
        add_desiredprice_slot3.config(fg='black')


def on_focusout_2_product4(event):
    if add_desiredprice_slot3.get() == '':
        add_desiredprice_slot3.insert(0, 'desired price here...')
        add_desiredprice_slot3.config(fg='grey')


add_url_slot3.bind('<FocusIn>', on_entry_click_product4)
add_url_slot3.bind('<FocusOut>', on_focusout_product4)
add_url_slot3.config(fg='grey')

add_desiredprice_slot3.bind('<FocusIn>', on_entry_click_2_product4)
add_desiredprice_slot3.bind('<FocusOut>', on_focusout_2_product4)
add_desiredprice_slot3.config(fg='grey')

# Read previously entered values after restarting the application.
try:
    file_prev = open('pricetracker.txt', 'r')
    fp = file_prev.readlines()

    if fp[0] == '.\n':
        pass
    else:
        add_url_slot.delete(0, END)
        add_desiredprice_slot.delete(0, END)
        add_url_slot.insert(0, fp[0].split('|')[0])
        add_desiredprice_slot.insert(0, fp[0].split('|')[1][:-1])
        add_url_slot.config(state='readonly')
        add_desiredprice_slot.config(state='readonly')

    if fp[1] == '.\n':
        pass
    else:
        add_url_slot1.delete(0, END)
        add_desiredprice_slot1.delete(0, END)
        add_url_slot1.insert(0, fp[1].split('|')[0])
        add_desiredprice_slot1.insert(0, fp[1].split('|')[1][:-1])
        add_url_slot1.config(state='readonly')
        add_desiredprice_slot1.config(state='readonly')

    if fp[2] == '.\n':
        pass
    else:
        add_url_slot2.delete(0, END)
        add_desiredprice_slot2.delete(0, END)
        add_url_slot2.insert(0, fp[2].split('|')[0])
        add_desiredprice_slot2.insert(0, fp[2].split('|')[1][:-1])
        add_url_slot2.config(state='readonly')
        add_desiredprice_slot2.config(state='readonly')

    if fp[3] == '.\n':
        pass
    else:
        add_url_slot3.delete(0, END)
        add_desiredprice_slot3.delete(0, END)
        add_url_slot3.insert(0, fp[3].split('|')[0])
        add_desiredprice_slot3.insert(0, fp[3].split('|')[1][:-1])
        add_url_slot3.config(state='readonly')
        add_desiredprice_slot3.config(state='readonly')

except:
    pass

root.mainloop()
