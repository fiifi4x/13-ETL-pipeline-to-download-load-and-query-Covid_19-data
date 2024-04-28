Gathering requirements





10Alytics Data Engineer Capstone Project
Part 1 (SQL)
Introduction:
The Covid 19 pandemic has wreaked havoc and led to the dramatic loss of lives and
livelihoods. Its impact continues to affect the way in we live and interact. In this
project, you will analyze sample data related to COVID-19 cases as recorded from
January 2019 to December, 2020.
The data is provided as a CSV file.
Data Summary:

Instructions:
NB: The you’re expected to use PostgreSQL as your database tool.
Follow this link to download, install and setup a Postgresql database If you don’t currently have Postgresql installed: https://www.postgresqltutorial.com/installpostgresql/
1. Create a database and a table called covid_19_data to hold the data in postgresql.
2. You’re to define the data type of ObservationDate as DATE type in the database instead of String as shown on the data summary image above.
3. Use a python script to download the Covid_19_data.csv file and load into a Postgresql database.
4. Use the Posgresql PG4 Admin for writing and running your SQL Queries.
5. You will submit only one SQL file with all the queries.

Your task:
1. Write a simple Python script to download the Covid_19_data.csv file using this link .
2. The script should also be used to load the data into the table you created in a PostgreSQL Database.
3. Write suitable sql queries to analyze and generate insight from the data.

Below are the questions you are to write SQL queries to find answers to:
1. Retrieve the total confirmed, death, and recovered cases.
2. Retrieve the total confirmed, deaths and recovered cases for the first quarter
of each year of observation.
3. Retrieve a summary of all the records. This should include the following
information for each country:
● The total number of confirmed cases
● The total number of deaths
● The total number of recoveries
4. Retrieve the percentage increase in the number of death cases from 2019 to
2020.
5. Retrieve information for the top 5 countries with the highest confirmed cases.
6. Compute the total number of drop (decrease) or increase in the confirmed
cases from month to month in the 2 years of observation.
Submission:
You’re required to put all the queries in a single .sql file. Then create a repository on
Github to host your project. Your repo should contain:
1. A single SQL file containing all the queries.
2. A folder in the repository called “outputs”. This folder should contain screenshots
of the outputs from running the queries.
3. A single python file for downloading and loading the data into PostgreSQL.
Finally, you will submit a link to the Github repository.