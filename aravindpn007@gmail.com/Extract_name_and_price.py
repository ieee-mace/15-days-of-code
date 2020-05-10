# About the Project: Web Scraping Using Python - Track prices of products in Amazon.in

# Objective is to build a Python Script that helps us to track the price of a product that we wish to buy,
# so that we need not check the website all the time to see whether the price has dropped and instead Python will
# take care of it!


from bs4 import BeautifulSoup as Soup
import requests

url = 'https://www.amazon.in/Casio-G-Shock-Analog-Digital-Watch-GA-700CM-3ADR-G824/dp/B07B4SZ1FL/ref' \
      '=lp_21488213031_1_5?s=watches&ie=UTF8&qid=1589103008&sr=1-5 '

user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/81.0.4044.138 Safari/537.36'}
page = requests.get(url, headers=user_agent)

page_content = Soup(page.content, 'html.parser')
page.close()

product_name = page_content.find('span', {'id': 'productTitle'}).text.strip()

price = page_content.find('span', {'id': 'priceblock_ourprice'}).text
value = float(price.replace(',', '')[2:])

print(product_name)
print(price)
