# SQL-Alchemy

In this assignment, Python and SQLAlchemy were used to do a basic climate analysis and data exploration of a climate database. Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib were used. 
.

**Part 1: Analyze and Explore the Climate Data**

1. For the climate_starter files, used the SQLAlchemy create_engine() function to connect to the SQLite database.
   
2. Used the SQLAlchemy automap_base() function to reflect the tables into classes, and then saved references to the classes named _station_ and _measurement_.
   
3. Linked Python to the database by creating a SQLAlchemy session

*Precipitation Analysis*

1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method, as the following image shows:
7. Use Pandas to print the summary statistics for the precipitation data.

![image](https://github.com/AishHen/SQL-Alchemy/assets/131278014/903dc384-ee8f-4ef2-bdee-30ca31e9876c)


*Station Analysis*

1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
3. List the stations and observation counts in descending order.
4. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
5. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
6. Filter by the station that has the greatest number of observations.
7. Query the previous 12 months of TOBS data for that station.
8. Plot the results as a histogram with bins=12

   ![image](https://github.com/AishHen/SQL-Alchemy/assets/131278014/5c763c05-6007-478c-95d6-f9385573137c)


**Part 2: Design Your Climate App**

*With the initial analysis completed, a Flask API was designed based on the queries in Part 1.* 

1. Start at the homepage.

2. List all the available routes.

3. Convert the query results from the precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

4. Return the JSON representation of your dictionary.

5. Return a JSON list of stations from the dataset.

6. Query the dates and temperature observations of the most-active station for the previous year of data.

7. Return a JSON list of temperature observations for the previous year.

8. Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

9. For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

10. For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


Resources: AskBCS Assistance with bar chart 
