# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#1. Define welcome page
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Starter<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#2. Set route for precipitation 
@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precip_query = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_ago).all()

    session.close()

    # Create dictionary
    precipitation = {}
    for date, prcp in precip_query:
        precipitation[date] = prcp
        

    """Return the JSON representation of the dictionary"""
    return jsonify(precipitation)

#3. Set route for station data
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # Query for dictionary of stations
    stat_query = session.query(station.station).\
    order_by(station.station).all()

    session.close()

    # Create List 
    station_list = list(np.ravel(stat_query))

    """Return the JSON list of stations from the dataset"""
    return jsonify(station_list)

#4. Set route for temperature observations
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Using the most active station id
    # Query the last 12 months of temperature observation data for this station and plot the results as a histogram
    station_data = session.query(measurement.tobs).\
    filter(measurement.station == 'USC00519281').\
    filter(measurement.date >= year_ago).all()

    session.close()

    # List comprehension to store first item in dataset for graphing
    temperatures = [station_data[0] for station_data in station_data]
        
    """Return a JSON list of temperature observations for the previous year"""
    return jsonify(temperatures)

#5. Set route for start date
@app.route("/api/v1.0/start")
def start():
    session = Session(engine)

    #Run Query
    sel2 = [measurement.station,
        func.min(measurement.tobs),
        func.max(measurement.tobs),
        func.avg(measurement.tobs)]
    
    station_summary = session.query(*sel2).\
        filter(measurement.station =='USC00519281').all()
    session.close()

    #Create dictionary of values
    temp_stats = {"TMIN": station_summary[0][1],"TMAX": station_summary[0][2], "TAVG": station_summary[0][3]}

    return jsonify(temp_stats)
    

#6. Set route for start/end date 
@app.route("/api/v1.0/<start>/<end>")
def end():
     #Run Query
    sel2 = [measurement.station,
        func.min(measurement.tobs),
        func.max(measurement.tobs),
        func.avg(measurement.tobs)]
    
    station_summary = session.query(*sel2).\
        filter(measurement.station =='USC00519281').all()
    session.close()

    #Create dictionary of values
    temp_stats = {"TMIN": station_summary[0][1],"TMAX": station_summary[0][2], "TAVG": station_summary[0][3]}

    return jsonify(temp_stats)

if __name__ == "__main__":
    app.run(debug=True)
