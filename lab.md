# Practice Lab: Build a Data Pipeline for Census Data

In this practice lab, you will build a data pipeline using Apache Airflow to extract census data, transform it, and load it into a database based on certain conditions.

## Learning Objectives:

* Create tasks to extract, transform, and load data
* Handle missing data while transforming
* Load filtered data into a database based on conditions

## Steps:

1. Create a new DAG called census_data_pipeline
1. Define a PythonOperator to download the census CSV data from:
    ```
    https://raw.githubusercontent.com/practical-bootcamp/week4-assignment1-template/main/city_census.csv
    ```
1. Read in the CSV data and handle any missing values.
1. Filter the data and choose a condition to extract specific data. For example:
    * Age is greater than 30
    * State is 'Iowa'
1. Parse the data into a clean DataFrame and store it in a database
1. Set up the task ordering and dependencies correctly
1. Monitor the pipeline execution in the Airflow UI

**Bonus challenge:** Perform validation on the number of rows before loading into the database and add some simple statistics about the data as a final step.


By completing this lab, you will gain practical hands-on experience building a real-world data pipeline with Airflow. The skills covered, including data ingestion, transformation, orchestration, and database loading, will align directly with real-world data engineering pipelines. This lab will allow you to apply the Airflow concepts from the course to an end-to-end pipeline development scenario.
