# Assignment_Siddhesh

Author: Siddhesh Bagwe

The Assignment is broken into two parts.

# Part 1 AgriIQ Data Scraper

scraping_Siddhesh.py is a Python script for scraping agricultural market data from the [Agmarknet website](https://agmarknet.gov.in/) and storing it in a PostgreSQL database.

## Getting Started

These instructions will help you get the project up and running on your local machine.

## Prerequisites

- Python 3.x
- PostgreSQL database
- Required Python packages (install using `pip`):

  ```bash
  pip install requests beautifulsoup4 pandas psycopg2
  
## Usage
--commodity: Specify the commodity you want to scrape.

--start_date: Specify the start date for scraping data.

--end_date: Specify the end date for scraping data.

--time_agg: Specify the time aggregation.

--states: Specify the states for which you want to scrape data.

Run the script below to run the file

```bash
python scraping_Siddhesh.py --commodity=Onion --start_date=01-Jan-2020 --end_date=12-Apr-2022 --time_agg=monthly --states=Maharashtra
```

## SQL

Write a single SQL query to return the top 5 states for 4 commodities (Potato, Onion, Wheat, tomato) – Output should contain 20 records only



# Part-2 Milkrun Prediction Project

## Overview

This project aims to predict transit ETA for Milkrun deliveries.

## Libraries Used

- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

## Exploratory Data Analysis

- Dataset Info
- Data Preprocessing
- Data Visualization

## Feature Engineering

- Date and Time Conversion
- Data Correlation Analysis

## Model Building

- Linear Regression Model
- Model Evaluation (MSE, MAE, R-squared)

## Usage

- Clone the repository.
- Install required libraries.
- Run the Jupyter Notebook to see the project in action.
