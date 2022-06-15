from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
from flask_pymongo import pymongo

import scrape_mars
import sys



# import sys

app = Flask(__name__)

# mongo = PyMongo(app, uri="mongodb://localhost:27017/")
# setup mongo connection
conn = 'mongodb://localhost:27017'

# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_db

# mongo = PyMongo(app)


@app.route("/")
def index():
    print("I am on index.html")
    # write a statement that finds all the items in the db and sets it to a variable
    mars = collection.db.mars.find_one()
    print (mars)
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = collection.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)