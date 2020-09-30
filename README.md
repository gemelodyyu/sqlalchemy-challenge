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


### Routes



### Trip Temperature Analysis II


### Daily Rainfall Average


