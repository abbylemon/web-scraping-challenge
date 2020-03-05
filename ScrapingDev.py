


from bs4 import BeautifulSoup
from splinter import Browser
import time

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
    

    product_links = []
    product_images = []
    product_titles = []
    product_star_reviews = []
    product_prices = []

    for product in products:

        link = product.find('a')
        href = link['href']
        product_link = 'https://www.walmart.com' + href
        # print(product_link)
        product_links.append(product_link)
        # print('----->found link<-----')

        img = product.find('img')['src']
        # print(img)
        product_images.append(img)
        # print('----->found image<-----')

        product_title = product.find('img')['alt']
        # print(product_title)
        product_titles.append(product_title)
        # print('----->found title<-----')

        stars_review = product.find('span', class_='stars-container')['aria-label']   
        # print(stars_review)
        product_star_reviews.append(stars_review)
        # print('----->found stars and reviews<-----')

        price = product.find('span', class_='price-main')
        current_price = price.find('span', class_='visuallyhidden').text
        # print(current_price)
        product_prices.append(current_price)
        # print('----->found price<-----')

        print(f"----->scraped product {product_title}<-----")

    #     browser.click_link_by_partial_href(href)

    product_data = {
        "Link": product_links,
        "Image": product_images,
        "Name": product_titles,
        "Num_Stars_Reviews": product_star_reviews,
        "Price": product_prices
    }

    browser.quit()
    print('----->exit broswer<-----')

    return product_data
    print("----->returned data<-----")

# review = soup.find('div', class_='CustomerReviews-list')
# print(review)




