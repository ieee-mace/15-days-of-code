# About the Project: Web Scraping Using Python - Track prices of products in Amazon.in

# Objective is to build a Python Script that helps us to track the price of a product that we wish to buy,
# so that we need not check the website all the time to see whether the price has dropped and instead Python will
# take care of it!


from bs4 import BeautifulSoup as Soup
import requests
import smtplib


def grab_price():
    url = 'https://www.amazon.in/Casio-G-Shock-Analog-Digital-Watch-GA-700CM-3ADR-G824/dp/B07B4SZ1FL/ref' \
          '=lp_21488213031_1_5?s=watches&ie=UTF8&qid=1589103008&sr=1-5 '

    # Search 'my user agent' in the browser(to get your user agent) and copy and paste it in the variable
    # in the format {'User-Agent: 'Paste here'}
    user_agent = 'Your user agent'
    page = requests.get(url, headers=user_agent)

    page_content = Soup(page.content, 'html.parser')
    page.close()

    product_name = page_content.find('span', {'id': 'productTitle'}).text.strip()

    price = page_content.find('span', {'id': 'priceblock_ourprice'}).text
    value = float(price.replace(',', '')[2:])

    print(product_name)
    print(value)

    if value <= 7000:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smt.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    # Type your email id and the password...
    server.login('mail', 'password')

    msg = 'Price dropped, click the link below!'
    url = 'https://www.amazon.in/Casio-G-Shock-Analog-Digital-Watch-GA-700CM-3ADR-G824/dp/B07B4SZ1FL/ref' \
          '=lp_21488213031_1_5?s=watches&ie=UTF8&qid=1589103008&sr=1-5 '

    message = f'{msg}\n\n{url}'

    server.sendmail('from_mail', 'to_mail', message)
    print('Email has been sent..!')

    server.quit()


grab_price()
