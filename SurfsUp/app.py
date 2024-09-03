# Import the dependencies.
import numpy as np
import flask 
print(flask.__version__)
import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
last_twelve_months = '2016-08-23'
#################################################
# Flask Routes
#################################################
@app.route("/") 
def welcome():
    return (
        f"Welcome to the Hawaii API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"   
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
    )

# Convert the query results from your precipitation analysis 
# (i.e. retrieve only the last 12 months of data) to a dictionary using 
# date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Date 12 months ago
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)

    # Perform a query to retrieve the data and precipitation scores
    result = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date>=prev_year).all()

    return jsonify(result)

@app.route("/api/v1.0/stations")
def stations():
    return "Stations"

@app.route("/api/v1.0/tobs")
def tobs():
    return "Tobs"

@app.route("/api/v1.0/start_date/end_date")
def end():
    return "start end"

if __name__ == "__main__":
    app.run(debug=True)