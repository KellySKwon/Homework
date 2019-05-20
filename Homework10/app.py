from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def home():
    listings = mongo.db.listings.find_one()

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scraper():
    listings = mongo.db.listings
    listings_data = scrape_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
