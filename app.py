import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Create session link from Python to DB
session = Session(engine)

# find out the last date
last_date = (session.query(Measurement.date).order_by(Measurement.date.desc()).first())
# convert query object to string then to date formate
last_date = list(np.ravel(last_date))[0]
last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
# extract year, month, day of last date 
last_d_year = int(dt.datetime.strftime(last_date, "%Y"))
last_d_month = int(dt.datetime.strftime(last_date, "%m"))
last_d_day = int(dt.datetime.strftime(last_date, "%d"))
# calculate the date 1 year ago
year_ago = dt.date(last_d_year, last_d_month, last_d_day) - dt.timedelta(days=365)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation(): 
    """Convert the query results to a dictionary using date as the key and prcp as the value.
    Return the JSON representation of your dictionary."""

    print("Printing precipitation information of last 12 month...")

    # Create session link from Python to DB
    session = Session(engine)

    # Perform a query to retrieve the data and precipitation scores
    prcp_result = session.query(Measurement.prcp, Measurement.date).\
                        filter(Measurement.date >= year_ago).\
                        filter(Measurement.date <= last_date).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of precipitation_list
    precipitation_list = []
    for result in prcp_result: 
        prcp_data = {result.date: result.prcp}
        precipitation_list.append(prcp_data)

    return jsonify(precipitation_list)


@app.route("/api/v1.0/stations")
def stations(): 
    """Return a JSON list of stations from the dataset."""

    print("Printing stations information...")

    # Create session link from Python to DB
    session = Session(engine)

    # Query all stations
    sta_result = session.query(Station).all()

    session.close()

    # Create a dictionary from the row data and append to a list of station_list
    station_list = []
    for result in sta_result:
        all_station = {}
        all_station["id"] = result.id
        all_station["station"] = result.station
        all_station["name"] = result.name
        all_station["latitude"] = result.latitude
        all_station["longitude"] = result.longitude
        all_station["elevation"] = result.elevation
        station_list.append(all_station)

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs(): 
    """Query the dates and temperature observations of the most active station for the last year of data.
    Return a JSON list of temperature observations (TOBS) for the previous year."""

    print("Printing temperature observations for the previous year...")

    # Create session link from Python to DB
    session = Session(engine)

    # Query
    # List the stations and the counts in descending order.
    active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
                                    group_by(Measurement.station).\
                                    order_by(func.count(Measurement.station).desc()).all()

    # identify the most active station
    most_station = active_stations[0][0]
    # Query the last 12 months of temperature observation data for this station 
    tobs_result = session.query(Measurement.tobs, Measurement.date).\
                    filter(Measurement.station==most_station).\
                    filter(Measurement.date >= year_ago).\
                    filter(Measurement.date <= last_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of tob_list
    tobs_list = []
    for result in tobs_result: 
        tobs_data = {result.date: result.tobs}
        tobs_list.append(tobs_data)

    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start_date(start): 
    """Return a JSON list of the minimum temperature, the average temperature, 
    and the max temperature for a given start range."""

    print("Printing data since...")

    # Create session link from Python to DB
    session = Session(engine)

    # Query
    range_start = session.query(Measurement.date, func.min(Measurement.tobs), \
                func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()

    session.close()

    # Create a list to save results
    start_list = []                       
    for result in range_start:
        temp_list = {}
        temp_list["TMIN"] = result[1]
        temp_list["TAVG"] = result[2]
        temp_list["TMAX"] = result[3]
        start_list.append(temp_list)

    return jsonify(start_list)


@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end): 
    """Return a JSON list of the minimum temperature, the average temperature, 
    and the max temperature for a given start-end range."""

    print("Printing data from ... to ...")

    # Create session link from Python to DB
    session = Session(engine)

    # Query
    range_start_end = session.query(Measurement.date, func.min(Measurement.tobs), \
                func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
    
    session.close()

    # Create a list to save results
    start_end_list = []
    for result in range_start_end: 
        temp_list2 = {}
        temp_list2["TMIN"] = result[1]
        temp_list2["TAVG"] = result[2]
        temp_list2["TMAX"] = result[3]
        start_end_list.append(temp_list2)

    return jsonify(start_end_list)


if __name__ == '__main__':
    app.run(debug=True)
    