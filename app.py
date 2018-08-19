from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
from scrape import scraped

data_to_insert = scraped()

print(data_to_insert)

client = MongoClient('localhost', 27017)
db = client.mars 
coll = db.mars

coll.insert_one(data_to_insert)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars 
    mars_data = data_to_insert
    mars.update({}, mars_data, upsert=True)
    return redirect("http://localhost:27017/mars", code=302)

if __name__ == "__main__":
    app.run(debug=True)

