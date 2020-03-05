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
def echo():
    return render_template("index.html", text="Scraped Walmart RAP Info")

    print("----->displaying title<-----")

    product_info = list(collection.find())    

    return render_template("index.html", walmart_product=product_info)
    
    print("----->displayed data on page<-----")

@app.route("/scrape")
def scrape():


    # run the scrape
    product_data = ScrapingDev.scrape_info()
    print('----->scraping finished<-----')

    # update the database
    mongo.db.collection.update({}, product_data, upsert=True)
    print('----->loaded data into mongo<-----')

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)