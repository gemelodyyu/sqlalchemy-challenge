# SQLAlchemy Challenge - Surfs Up!


Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.


## Step 1 - Climate Analysis and Exploration


To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


### Precipitation Analysis


* Design a query to retrieve the last 12 months of precipitation data.


* Select only the date and prcp values.


* Load the query results into a Pandas DataFrame and set the index to the date column.


* Sort the DataFrame values by date.


* Plot the results using the DataFrame plot method.


![precipitation](https://user-images.githubusercontent.com/55970064/94644098-05373000-02ae-11eb-96d9-cfbeaccf207b.png)


* Use Pandas to print the summary statistics for the precipitation data.


 <img width="152" alt="Screen Shot 2020-09-29 at 23 48 09" src="https://user-images.githubusercontent.com/55970064/94644187-3ca5dc80-02ae-11eb-8712-9ecd0e11a03f.png">


### Station Analysis


* Design a query to calculate the total number of stations.


* Design a query to find the most active stations.


  * List the stations and observation counts in descending order.


  * Which station has the highest number of observations?



* Design a query to retrieve the last 12 months of temperature observation data (TOBS).


 * Filter by the station with the highest number of observations.


 * Plot the results as a histogram with bins=12.
 
 
 ![tobs](https://user-images.githubusercontent.com/55970064/94644464-fdc45680-02ae-11eb-9b01-fd6f7fa3f480.png)



## Step 2 - Climate App


Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.


### Routes


* /


  * Home page.


  * List all routes that are available.




* /api/v1.0/precipitation


  * Convert the query results to a dictionary using date as the key and prcp as the value.


  * Return the JSON representation of your dictionary.




* /api/v1.0/stations

  * Return a JSON list of stations from the dataset.



* /api/v1.0/tobs


  * Query the dates and temperature observations of the most active station for the last year of data.


  * Return a JSON list of temperature observations (TOBS) for the previous year.




* /api/v1.0/<start> and /api/v1.0/<start>/<end>


  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


  * When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


  * When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.


### Trip Temperature Analysis 


* The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.


* Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year.


* Plot the min, avg, and max temperature from your previous query as a bar chart.


  * Use the average temperature as the bar height.


  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).


![avg_temp](https://user-images.githubusercontent.com/55970064/94645007-59dbaa80-02b0-11eb-9600-58fc5b48d3fd.png)


