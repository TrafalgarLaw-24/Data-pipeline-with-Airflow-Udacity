# Data Pipeline With Airflow - Udacity

## Introduction

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

## What is Apache Airflow?
Airflow a workflow management system developed by Airbnb. It is a platform to programmatically author, schedule and monitor workflows.

As per the website:
Use airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

## Getting started

#### Built With

* [Python3](https://www.python.org/downloads/)
* [AWS](https://aws.amazon.com/) and [Redshift](https://aws.amazon.com/redshift/) cluster
* [Apache Airflow](https://airflow.apache.org/)

### Project Structure
```
airflow-data-pipeline
│   README.md                    # Project description
│   
└───airflow                      # Airflow home
|   |               
│   └───dags                     
│   |   │ udac_example_dag.py  	 # The DAG configuration file to run in Airflow
|   |   |
|   └───plugins
│       │  
|       └───helpers
|       |   | sql_queries.py     # Necessary sql queries
|       |
|       └───operators
|       |   | data_quality.py    # Data Quality Operator for checking data quality
|       |   | load_dimension.py  # Load Dimension Operator to read from staging tables and load the dimension tables in Redshift
|       |   | load_fact.py       # Load Fact Operator to load the fact table in Redshift
|       |   | stage_redshift.py  # Stage To Redshift Operator to read files from S3 and load into Redshift staging tables
|   |   |
|   └───create_tables.sql		 # Contains the DDLs of all the tables used in this project

```
## Data Source

Data resides in two directories of udacity buckets that contains files in JSON format:

Log data: s3://udacity-dend/log_data
Song data: s3://udacity-dend/song_data

## About
This project is done as part of Udacity Data Engineer Nano degree program
