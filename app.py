# impore libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import ScrapingDev

# create instance of Flask app
app = Flask(__name__)

# create the Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/walmart_product_db")

# create route that renders index.html template
@app.route("/")
def home():

    print("----->HOME<-----")

    product_info = list(mongo.db.collection.find())

    return render_template("index.html", walmart_product=product_info, text="Scraped Walmart RAP Info")

@app.route("/scrape")
def scrape():


    # run the scrape
    product_data = ScrapingDev.scrape_info()
    print('----->scraping finished<-----')

    # update the database
    col = mongo.db.collection

    # col.drop()
    for item in product_data:
        col.update_one(
            {'Name':item['Name']},
            {
                '$set': {
                    'Link':item['Link'],
                    'Image':item['Image'],
                    'Num_Stars_Reviews':item['Num_Stars_Reviews'],
                    'Price':item['Price']
                    }
            }, upsert=True)

    print('----->loaded data into mongo<-----')

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)