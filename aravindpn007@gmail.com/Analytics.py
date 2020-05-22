""" About the Project: Web Scraping Using Python - Track prices of products in Amazon.in

Objective is to build a Python Script that helps us to track the price of a product that we wish to buy,
so that we need not check the website all the time to see whether the price has dropped and instead Python will
take care of it! """

from bs4 import BeautifulSoup as Soup
import requests
from tkinter import *
import webbrowser
from tkinter import messagebox
import httpagentparser
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def grab_price(product_code):
    """ This function will extract name and price of the product, compares with your desired price and gives
    appropriate message """

    # Update the text file with user input data and assign values for url and desired price.
    try:
        filename = 'pricetracker.txt'
        file = open(filename, 'r')
        data = file.readlines()

        # last checked time

        TIME = str(datetime.datetime.now()).split()
        date = TIME[0]
        time = TIME[1]
        date_values = date.split('-')
        time_values = time.split(':')
        time_data = {'year': date_values[0], 'month': date_values[1], 'day': date_values[2],
                     'hour': time_values[0],
                     'min': time_values[1], 'sec': str(int(float(time_values[2])))}
        time_update = time_data['day'] + '/' + time_data['month'] + '/' + time_data['year'] + ' ' + time_data[
            'hour'] + ':' + time_data['min'] + ':' + time_data['sec'] + '\n'

        user_agent = data[4][:-1]
        url = url_list[product_code - 1].get()
        desired_price = price_list[product_code - 1].get()
        data[product_code - 1] = url + '|' + desired_price + '\n'
        data[5] = time_update
        file = open(filename, 'w')
        file.writelines(data)
        file.close()
        price_list[product_code - 1].config(state='readonly')
        url_list[product_code - 1].config(state='readonly')

        display_last_checked_time()

        user_agent_param = {'User-Agent': user_agent}

        # Try to extract data from Amazon.in
        try:
            page = requests.get(url, headers=user_agent_param)
            page_content = Soup(page.content, 'html.parser')
            page.close()
            product_name = page_content.find('span', {'id': 'productTitle'}).text.strip()
            if len(product_name) >= 90:
                product_name = product_name[0:91] + '....'

            # Check whether the product has a price
            try:
                price = page_content.find('span', {'id': 'priceblock_ourprice'}).text
                value = float(price.replace(',', '')[2:])
                fdata = open('pricetracker.txt', 'r')
                fdataval = fdata.readlines()
                if fdataval[product_code + 5][:-1] == '.':
                    fdataval[product_code + 5] = str(value) + ',' + '\n'
                else:
                    if len(fdataval[product_code + 5][:-2].split(',')) == 20:
                        fdataval[product_code + 5] = ','.join(fdataval[product_code + 5][:-2].split(',')[1:]) + ',' + str(value) + ',' + '\n'
                    else:
                        fdataval[product_code + 5] = fdataval[product_code + 5][:-1] + str(value) + ',' + '\n'
                fdata = open('pricetracker.txt', 'w')
                fdata.writelines(fdataval)
                fdata.close()
                # Display product name and price
                if product_code - 1 == 0:
                    global product_name_label
                    global message_label
                    product_name_label.destroy()
                    product_name_label = Label(frame1, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                               relief='solid')
                    product_name_label.grid(row=3, column=0, pady=5)

                elif product_code - 1 == 1:
                    global product_name_label1
                    global message_label1
                    product_name_label1.destroy()
                    product_name_label1 = Label(frame2, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                                relief='solid')
                    product_name_label1.grid(row=7, column=0, pady=5)

                elif product_code - 1 == 2:
                    global product_name_label2
                    global message_label2
                    product_name_label2.destroy()
                    product_name_label2 = Label(frame3, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                                relief='solid')
                    product_name_label2.grid(row=11, column=0, pady=5)

                elif product_code - 1 == 3:
                    global product_name_label3
                    global message_label3
                    product_name_label3.destroy()
                    product_name_label3 = Label(frame4, text="Product: " + product_name + '\nCurrent Price: ' + price,
                                                relief='solid')
                    product_name_label3.grid(row=15, column=0, pady=5)

                # Display appropriate message
                try:
                    if product_code - 1 == 0:
                        if value <= float(desired_price):
                            message_label.destroy()
                            message_label = Label(frame1, text='Price dropped!', fg='green')
                            message_label.grid(row=1, column=3)
                            visit_page_button.config(state=NORMAL)
                        else:
                            message_label.destroy()
                            message_label = Label(frame1, text='No price drop')
                            message_label.grid(row=1, column=3)
                            visit_page_button.config(state=NORMAL)

                    elif product_code - 1 == 1:
                        if value <= float(desired_price):
                            message_label1.destroy()
                            message_label1 = Label(frame2, text='Price dropped!', fg='green')
                            message_label1.grid(row=5, column=3)
                            visit_page_button1.config(state=NORMAL)
                        else:
                            message_label1.destroy()
                            message_label1 = Label(frame2, text='No price drop')
                            message_label1.grid(row=5, column=3)
                            visit_page_button1.config(state=NORMAL)

                    elif product_code - 1 == 2:
                        if value <= float(desired_price):
                            message_label2.destroy()
                            message_label2 = Label(frame3, text='Price dropped!', fg='green')
                            message_label2.grid(row=9, column=3)
                            visit_page_button2.config(state=NORMAL)
                        else:
                            message_label2.destroy()
                            message_label2 = Label(frame3, text='No price drop')
                            message_label2.grid(row=9, column=3)
                            visit_page_button2.config(state=NORMAL)

                    elif product_code - 1 == 3:
                        if value <= float(desired_price):
                            message_label3.destroy()
                            message_label3 = Label(frame4, text='Price dropped!', fg='green')
                            message_label3.grid(row=13, column=3)
                            visit_page_button3.config(state=NORMAL)
                        else:
                            message_label3.destroy()
                            message_label3 = Label(frame4, text='No price drop')
                            message_label3.grid(row=13, column=3)
                            visit_page_button3.config(state=NORMAL)

                # What if user entered an invalid price?
                except:
                    if product_code - 1 == 0:
                        message_label.destroy()
                        message_label = Label(frame1, text='Add a valid price', fg='red')
                        message_label.grid(row=1, column=3)
                        fd = open(filename, 'r')  # Delete the data stored in the text file.
                        d = fd.readlines()
                        d[product_code - 1] = '.\n'
                        fd = open(filename, 'w')
                        fd.writelines(d)
                        fd.close()
                        add_desiredprice_slot.config(state='normal')
                        add_url_slot.config(state='normal')

                    elif product_code - 1 == 1:
                        message_label1.destroy()
                        message_label1 = Label(frame2, text='Add a valid price', fg='red')
                        message_label1.grid(row=5, column=3)
                        fd = open(filename, 'r')
                        d = fd.readlines()
                        d[product_code - 1] = '.\n'
                        fd = open(filename, 'w')
                        fd.writelines(d)
                        fd.close()
                        add_desiredprice_slot1.config(state='normal')
                        add_url_slot1.config(state='normal')

                    elif product_code - 1 == 2:
                        message_label2.destroy()
                        message_label2 = Label(frame3, text='Add a valid price', fg='red')
                        message_label2.grid(row=9, column=3)
                        fd = open(filename, 'r')
                        d = fd.readlines()
                        d[product_code - 1] = '.\n'
                        fd = open(filename, 'w')
                        fd.writelines(d)
                        fd.close()
                        add_desiredprice_slot2.config(state='normal')
                        add_url_slot2.config(state='normal')

                    elif product_code - 1 == 3:
                        message_label3.destroy()
                        message_label3 = Label(frame4, text='Add a valid price', fg='red')
                        message_label3.grid(row=13, column=3)
                        fd = open(filename, 'r')
                        d = fd.readlines()
                        d[product_code - 1] = '.\n'
                        fd = open(filename, 'w')
                        fd.writelines(d)
                        fd.close()
                        add_desiredprice_slot3.config(state='normal')
                        add_url_slot3.config(state='normal')

            # Some products in Amazon doesn't have price information.
            except:
                if product_code - 1 == 0:
                    message_label.destroy()
                    product_name_label.destroy()
                    product_name_label = Label(frame1,
                                               text="Product: " + product_name + '\nCurrent Price: No price listed in Amazon',
                                               relief='solid', fg='red')
                    product_name_label.grid(row=3, column=0, pady=5)
                    fz = open(filename, 'r')
                    d = fz.readlines()
                    d[product_code - 1] = '.\n'
                    fz = open(filename, 'w')
                    fz.writelines(d)
                    fz.close()
                    add_desiredprice_slot.config(state='normal')
                    add_url_slot.config(state='normal')

                elif product_code - 1 == 1:
                    message_label1.destroy()
                    product_name_label1.destroy()
                    product_name_label1 = Label(frame2,
                                                text="Product: " + product_name + '\nCurrent Price: No price listed in Amazon',
                                                relief='solid', fg='red')
                    product_name_label1.grid(row=7, column=0, pady=5)
                    fz = open(filename, 'r')
                    d = fz.readlines()
                    d[product_code - 1] = '.\n'
                    fz = open(filename, 'w')
                    fz.writelines(d)
                    fz.close()
                    add_desiredprice_slot1.config(state='normal')
                    add_url_slot1.config(state='normal')

                elif product_code - 1 == 2:
                    message_label2.destroy()
                    product_name_label2.destroy()
                    product_name_label2 = Label(frame3,
                                                text="Product: " + product_name + '\nCurrent Price: No price listed in Amazon',
                                                relief='solid', fg='red')
                    product_name_label2.grid(row=11, column=0, pady=5)
                    fz = open(filename, 'r')
                    d = fz.readlines()
                    d[product_code - 1] = '.\n'
                    fz = open(filename, 'w')
                    fz.writelines(d)
                    fz.close()
                    add_desiredprice_slot2.config(state='normal')
                    add_url_slot2.config(state='normal')

                elif product_code - 1 == 3:
                    message_label3.destroy()
                    product_name_label3.destroy()
                    product_name_label3 = Label(frame4,
                                                text="Product: " + product_name + '\nCurrent Price: No price listed in Amazon',
                                                relief='solid', fg='red')
                    product_name_label3.grid(row=15, column=0, pady=5)
                    fz = open(filename, 'r')
                    d = fz.readlines()
                    d[product_code - 1] = '.\n'
                    fz = open(filename, 'w')
                    fz.writelines(d)
                    fz.close()
                    add_desiredprice_slot3.config(state='normal')
                    add_url_slot3.config(state='normal')

        except requests.exceptions.ConnectionError:
            messagebox.showerror('Error', 'Check your internet connection')

        # We need to ensure that a non-Amazon url is rejected.
        except:
            if product_code - 1 == 0:
                message_label.destroy()
                message_label = Label(frame1, text='Invalid url', fg='red')
                message_label.grid(row=1, column=3)
                fn = open(filename, 'r')
                d = fn.readlines()
                d[product_code - 1] = '.\n'
                fn = open(filename, 'w')
                fn.writelines(d)
                fn.close()
                add_desiredprice_slot.config(state='normal')
                add_url_slot.config(state='normal')

            elif product_code - 1 == 1:
                message_label1.destroy()
                message_label1 = Label(frame2, text='Invalid url', fg='red')
                message_label1.grid(row=5, column=3)
                fn = open(filename, 'r')
                d = fn.readlines()
                d[product_code - 1] = '.\n'
                fn = open(filename, 'w')
                fn.writelines(d)
                fn.close()
                add_desiredprice_slot1.config(state='normal')
                add_url_slot1.config(state='normal')

            elif product_code - 1 == 2:
                message_label2.destroy()
                message_label2 = Label(frame3, text='Invalid url', fg='red')
                message_label2.grid(row=9, column=3)
                fn = open(filename, 'r')
                d = fn.readlines()
                d[product_code - 1] = '.\n'
                fn = open(filename, 'w')
                fn.writelines(d)
                fn.close()
                add_desiredprice_slot2.config(state='normal')
                add_url_slot2.config(state='normal')

            elif product_code - 1 == 3:
                message_label3.destroy()
                message_label3 = Label(frame4, text='Invalid url', fg='red')
                message_label3.grid(row=13, column=3)
                fn = open(filename, 'r')
                d = fn.readlines()
                d[product_code - 1] = '.\n'
                fn = open(filename, 'w')
                fn.writelines(d)
                fn.close()
                add_desiredprice_slot3.config(state='normal')
                add_url_slot3.config(state='normal')

    except:
        def add_user_agent():
            """ New user should input their user agent """

            def valid_agent():
                """ Check if the entered user agent is valid """

                my_user_agent = enter_user_agent.get()
                information = httpagentparser.simple_detect(my_user_agent)
                if information[0] == 'Unknown OS' or information[1] == 'Unknown Browser':
                    messagebox.showerror('Error', 'Invalid User-Agent')
                    user_agent_window.destroy()
                    add_user_agent()
                else:
                    create_file = open('pricetracker.txt', 'w')
                    default_data = ['.\n', '.\n', '.\n', '.\n', '.\n', '.\n', '.\n', '.\n', '.\n', '.\n', '.']  # 6
                    default_data[4] = my_user_agent + '\n'
                    create_file.writelines(default_data)
                    create_file.close()
                    user_agent_window.destroy()

            # pop up window
            user_agent_window = Toplevel(root)
            user_agent_window.resizable(0, 0)
            info_label = Label(user_agent_window,
                               text='Welcome to Price Tracker App!\nBefore getting started, paste your user-agent below\n').pack()
            dont_know = Label(user_agent_window,
                              text="Search for 'my user agent' in your browser and it will show up first").pack()
            enter_user_agent = Entry(user_agent_window, width=60)
            enter_user_agent.pack(padx=10, pady=10)
            user_agent_window.title('Welcome!')
            OK = Button(user_agent_window, text='OK', command=valid_agent, padx=15).pack()
            user_agent_window.grab_set()

        add_user_agent()


def clear_product(product_code):
    """ Clears / resets all user input fields, clears pricetracker.txt file """

    filename = 'pricetracker.txt'
    if product_code - 1 == 0:
        global product_name_label
        global message_label
        try:
            fi = open(filename, 'r')
            d = fi.readlines()
            d[product_code - 1] = '.\n'
            d[product_code + 5] = '.\n'
            fi = open(filename, 'w')
            fi.writelines(d)
            fi.close()
            add_desiredprice_slot.config(state='normal')
            add_url_slot.config(state='normal')
            add_url_slot.delete(0, END)
            add_desiredprice_slot.delete(0, END)
            product_name_label.destroy()
            visit_page_button.config(state=DISABLED)
            message_label.destroy()
        except:
            grab_price(1)

    elif product_code - 1 == 1:
        global product_name_label1
        global message_label1
        try:
            fi = open(filename, 'r')
            d = fi.readlines()
            d[product_code - 1] = '.\n'
            d[product_code + 5] = '.\n'
            fi = open(filename, 'w')
            fi.writelines(d)
            fi.close()
            add_desiredprice_slot1.config(state='normal')
            add_url_slot1.config(state='normal')
            add_url_slot1.delete(0, END)
            add_desiredprice_slot1.delete(0, END)
            product_name_label1.destroy()
            visit_page_button1.config(state=DISABLED)
            message_label1.destroy()
        except:
            grab_price(1)

    elif product_code - 1 == 2:
        global product_name_label2
        global message_label2
        try:
            fi = open(filename, 'r')
            d = fi.readlines()
            d[product_code - 1] = '.\n'
            d[product_code + 5] = '.\n'
            fi = open(filename, 'w')
            fi.writelines(d)
            fi.close()
            add_desiredprice_slot2.config(state='normal')
            add_url_slot2.config(state='normal')
            add_url_slot2.delete(0, END)
            add_desiredprice_slot2.delete(0, END)
            product_name_label2.destroy()
            visit_page_button2.config(state=DISABLED)
            message_label2.destroy()
        except:
            grab_price(1)

    elif product_code - 1 == 3:
        global product_name_label3
        global message_label3
        try:
            fi = open(filename, 'r')
            d = fi.readlines()
            d[product_code - 1] = '.\n'
            d[product_code + 5] = '.\n'
            fi = open(filename, 'w')
            fi.writelines(d)
            fi.close()
            add_desiredprice_slot3.config(state='normal')
            add_url_slot3.config(state='normal')
            add_url_slot3.delete(0, END)
            add_desiredprice_slot3.delete(0, END)
            product_name_label3.destroy()
            visit_page_button3.config(state=DISABLED)
            message_label3.destroy()
        except:
            grab_price(1)


def open_page(product_code):
    """ Open the web page of the product in your default browser """

    webbrowser.open(url_list[product_code - 1].get())


root = Tk()  # Master window
root.resizable(0, 0)  # Maximize button is disabled
root.title('Price Tracker')

# Frames
frame1 = LabelFrame(root, text='Product 1', padx=10, pady=10, borderwidth=2)
frame1.grid(row=0, column=0, padx=10, pady=10)
frame2 = LabelFrame(root, text='Product 2', padx=10, pady=10, borderwidth=2)
frame2.grid(row=1, column=0, padx=10, pady=10)
frame3 = LabelFrame(root, text='Product 3', padx=10, pady=10, borderwidth=2)
frame3.grid(row=2, column=0, padx=10, pady=10)
frame4 = LabelFrame(root, text='Product 4', padx=10, pady=10, borderwidth=2)
frame4.grid(row=3, column=0, padx=10, pady=10)

status = Label(root, text='Developed by Aravind P N', relief=SUNKEN, anchor=E, fg='grey')  # Status bar
status.grid(row=101, column=0, columnspan=4, sticky=E + W)

# Product 1 labels

product_name_label = Label(frame1)
message_label = Label(frame1)

# Product 2 labels

product_name_label1 = Label(frame2)
message_label1 = Label(frame2)

# Product 3 labels

product_name_label2 = Label(frame3)
message_label2 = Label(frame3)

# Product 4 labels

product_name_label3 = Label(frame4)
message_label3 = Label(frame4)

# First Product

add_url_slot = Entry(frame1, width=100, borderwidth=3)
add_url_slot.grid(row=1, column=0)
add_url_slot.insert(0, 'paste url here...')

check_button = Button(frame1, text='Check', command=lambda: grab_price(1), padx=27)
check_button.grid(row=1, column=2)

add_desiredprice_slot = Entry(frame1, width=100, borderwidth=3)
add_desiredprice_slot.grid(row=2, column=0)
add_desiredprice_slot.insert(0, 'desired price here...')

remove_button = Button(frame1, text='Reset', fg='red', command=lambda: clear_product(1), padx=29)
remove_button.grid(row=2, column=2)

visit_page_button = Button(frame1, text='Visit Page', command=lambda: open_page(1), padx=15, fg='blue')
visit_page_button.grid(row=2, column=3)
visit_page_button.config(state=DISABLED)

# Second Product

add_url_slot1 = Entry(frame2, width=100, borderwidth=3)
add_url_slot1.grid(row=5, column=0)
add_url_slot1.insert(0, 'paste url here...')

check_button1 = Button(frame2, text='Check', command=lambda: grab_price(2), padx=27)
check_button1.grid(row=5, column=2)

add_desiredprice_slot1 = Entry(frame2, width=100, borderwidth=3)
add_desiredprice_slot1.grid(row=6, column=0)
add_desiredprice_slot1.insert(0, 'desired price here...')

remove_button1 = Button(frame2, text='Reset', fg='red', command=lambda: clear_product(2), padx=29)
remove_button1.grid(row=6, column=2)

visit_page_button1 = Button(frame2, text='Visit Page', command=lambda: open_page(2), padx=15, fg='blue')
visit_page_button1.grid(row=6, column=3)
visit_page_button1.config(state=DISABLED)

# Third Product

add_url_slot2 = Entry(frame3, width=100, borderwidth=3)
add_url_slot2.grid(row=9, column=0)
add_url_slot2.insert(0, 'paste url here...')

check_button2 = Button(frame3, text='Check', command=lambda: grab_price(3), padx=27)
check_button2.grid(row=9, column=2)

add_desiredprice_slot2 = Entry(frame3, width=100, borderwidth=3)
add_desiredprice_slot2.grid(row=10, column=0)
add_desiredprice_slot2.insert(0, 'desired price here...')

remove_button2 = Button(frame3, text='Reset', fg='red', command=lambda: clear_product(3), padx=29)
remove_button2.grid(row=10, column=2)

visit_page_button2 = Button(frame3, text='Visit Page', command=lambda: open_page(3), padx=15, fg='blue')
visit_page_button2.grid(row=10, column=3)
visit_page_button2.config(state=DISABLED)

# Fourth Product

add_url_slot3 = Entry(frame4, width=100, borderwidth=3)
add_url_slot3.grid(row=13, column=0)
add_url_slot3.insert(0, 'paste url here...')

check_button3 = Button(frame4, text='Check', command=lambda: grab_price(4), padx=27)
check_button3.grid(row=13, column=2)

add_desiredprice_slot3 = Entry(frame4, width=100, borderwidth=3)
add_desiredprice_slot3.grid(row=14, column=0)
add_desiredprice_slot3.insert(0, 'desired price here...')

remove_button3 = Button(frame4, text='Reset', fg='red', command=lambda: clear_product(4), padx=29)
remove_button3.grid(row=14, column=2)

visit_page_button3 = Button(frame4, text='Visit Page', command=lambda: open_page(4), padx=15, fg='blue')
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

# frame for check all and reset all
crall_frame = LabelFrame(root, padx=10, pady=10, borderwidth=2)
crall_frame.grid(row=4, column=0, padx=10, sticky=E + W)


# Check all products
def check_all():
    """ Checks price of all the entered products """

    try:
        fc = open('pricetracker.txt', 'r')
        for i in range(1, 5):
            grab_price(i)
    except:
        grab_price(1)


check_all_button = Button(crall_frame, text='Check all', command=check_all)
check_all_button.grid(row=99, column=0)


# Reset all products
def reset_all():
    """ Resets all the input fields """

    try:
        fr = open('pricetracker.txt', 'r')
        for i in range(1, 5):
            clear_product(i)
    except:
        grab_price(1)


reset_all_button = Button(crall_frame, text='Reset all', command=reset_all, fg='red')
reset_all_button.grid(row=99, column=1, padx=10)

# display last checked time
try:
    f = open('pricetracker.txt', 'r')
    info = f.readlines()[5][:-1]
    f.close()
except:
    info = '.'

# last checked time display
time_label = Label(root, text='Last checked: ' + info, fg='grey', anchor=W)
time_label.grid(row=100, column=0, pady=5, sticky=E + W, padx=5)


def display_last_checked_time():
    """ Reads previously checked time, and displays it on the interface """

    global time_label
    file = open('pricetracker.txt')
    time_data = file.readlines()
    time = time_data[5][:-1]
    time_label.destroy()
    time_label = Label(root, text='Last checked: ' + time, fg='grey', anchor=W)
    time_label.grid(row=100, column=0, pady=5, sticky=E + W, padx=5)


def analytics_product1(code):
    try:
        fp1 = open('pricetracker.txt', 'r')
        data_analytics = fp1.readlines()
        if data_analytics[5 + code][:-1] == '.':
            p1_values = [np.NaN]
        else:
            p1_values = list(map(float, data_analytics[5 + code][:-2].split(',')))
        nan_reqd1 = 20 - len(p1_values)
        modified_p1_values = p1_values + ([np.NaN] * nan_reqd1)
        fp1.close()
        df1 = pd.DataFrame(modified_p1_values, columns=['Product' + str(code)],
                           index='1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'.split())
        df1.plot(color='red')
        plt.show()

    except:
        grab_price(1)


Launch = Button(root, text='LAUNCH', command=lambda: analytics_product1(1))
Launch.grid(row=105, column=0)

root.mainloop()
