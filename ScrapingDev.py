from bs4 import BeautifulSoup
from splinter import Browser
import time
import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.walmart_product_db
collection = db.collection

# get_ipython().system('which chromdriver')

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = "https://www.walmart.com/search/?query=room%20air%20purifier"
    browser.visit(url)
    print('----->opened query search<-----')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', class_='search-result-gridview-item')

    product_data = []

    for product in products:

        try:
            link = product.find('a')
            href = link['href']
            product_link = 'https://www.walmart.com' + href

            img = product.find('img')['src']

            product_title = product.find('img')['alt']

            stars_review = product.find('span', class_='stars-container')['aria-label']   

            price = product.find('span', class_='price-main')
            current_price = price.find('span', class_='visuallyhidden').text

            print(f"----->scraped product {product_title}<-----")

        except:
            pass

        data = {
            "Link": product_link,
            "Image": img,
            "Name": product_title,
            "Num_Stars_Reviews": stars_review,
            "Price": current_price
        }

        product_data.append(data)

        '''
        find the element where the next button is, find_by_css? 
        then at the end use .click() function to lick on that element
        '''
        # browser.find_by_css("paginator-btn-next").click()
        # browser.find_element_by_class_namer("paginator-btn-next").click()
        # browser.find_element_by_name("paginator-btn-next").click()
        # browser.find_by_css("button").click()
        # browser.click_link_by_text(page_number)
        # browser.find_by_css('button').first.click()

    browser.quit()
    print('----->exit broswer<-----')
    print(html)
    return product_data




