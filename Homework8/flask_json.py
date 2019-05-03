import numpy as np
import datetime as dt
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, Column, Integer, String, Float, and_, or_, distinct
from sqlalchemy.sql import label

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
# @TODO: Initialize your Flask app here
app = Flask(__name__)

#################################################
# Flask Routes
#################################################


@app.route("/")
def home():
    #prints on terminal
    print("Server received request for 'Home' page...")
    #this returns on webpage
    return "Welcome to my 'Home' page!"

@app.route("/api/v1.0/precipitation")
def date():
    # Query all date, precipation
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Convert list of tuples into normal list
    all_dates = (result[0] for result in results)
    all_prcp = (result[1] for result in results)

    # Convert result to dictionary using date as key and prcp as value
    prcp_dict = dict(zip(all_dates,all_prcp))
    
    # Return on webpage
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def station():
    # Query all stations
    results = session.query(Station.station).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    
    # Return on webpage
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temp():
    """ From Exploratory Climate Analysis, last data point in the database is 2017-08-23 """
    
    #Query temp from a year from last data point
    query = session.query(func.max(Measurement.date)).first()
    maxDate = dt.datetime.strptime(query[0],'%Y-%m-%d')
    year_ago = maxDate - dt.timedelta(days=365)

    results = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date>=year_ago).all()

    # convert list of tuples into normal list
    all_dates = (result[0] for result in results)
    all_tobs = (result[1] for result in results)

    # Convert result to dictionary using date as key and tobs as value
    tobs_dict = dict(zip(all_dates,all_tobs))

    # Return on webpage
    return jsonify(tobs_dict)


@app.route("/api/v1.0/<start>")
def start(start=None):

    # Get user input and format as date
    UserDate = dt.datetime.strptime(start, '%Y-%m-%d')

    # Get range start and end dates (1 year before and after input)
    startDate = UserDate - dt.timedelta(days=365)
    endDate = UserDate + dt.timedelta(days=365)

    # Query TMIN, TAVG, and TMAX based on start and end date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= startDate).all()
    
    summary = list(np.ravel(results))
    return jsonify(summary)

@app.route("/api/v1.0/<start>/<end>")
def startend(start=None,end=None):

    # Get user input and format as date
    UserDate = dt.datetime.strptime(start, '%Y-%m-%d')

    # Get range start and end dates (1 year before and after input)
    startDate = UserDate - dt.timedelta(days=365)
    endDate = UserDate + dt.timedelta(days=365)

    # Query TMIN, TAVG, and TMAX based on start and end date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= startDate).filter(Measurement.date <= endDate).all()
    
    summary = list(np.ravel(results))
    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)