# -*- coding: utf-8 -*-
import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
from psycopg2 import sql

# Function to scrape and process data
def scrape_agmarket(commodity, start_date, end_date, time_agg,state):
    try:
            base_url = "https://agmarknet.gov.in/"  
            if state == "Maharashtra":
                url = f"{base_url}SearchCmmMkt.aspx?Tx_State=MH&Tx_Commodity=23&Tx_District=0&Tx_Market=0&DateFrom={start_date}&DateTo={end_date}&Fr_Date={start_date}&To_Date={end_date}&Tx_Trend=0&Tx_CommodityHead={commodity}&Tx_StateHead={state}&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--"
                response = requests.get(url)
                
            else:
                url = f"{base_url}SearchCmmMkt.aspx?Tx_State=WB&Tx_Commodity=23&Tx_District=0&Tx_Market=0&DateFrom={start_date}&DateTo={end_date}&Fr_Date={start_date}&To_Date={end_date}&Tx_Trend=0&Tx_CommodityHead={commodity}&Tx_StateHead={state}&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--"
                response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract and process the data from the HTML table
                table = soup.find('table', {'class': 'tableagmark_new'})
                df = pd.read_html(str(table), header=0)[0]
                state = state.replace('+',' ')
                df['state'] = state
                df.dropna(inplace=True)
                
                # Save the DataFrame as a CSV file
                csv_file_name = 'agmarket_data.csv'
                df.to_csv(csv_file_name, index=False)

                #Connect to the PostgreSQL database
                conn = psycopg2.connect(
                    database="agriiq",
                    user="postgres",
                    password="siddhesh",
                    host="localhost"  
                )

                #Insert data into the database
                cursor = conn.cursor()
                for _, row in df.iterrows():
                    cursor.execute(sql.SQL("INSERT INTO agmarket_monthly (sl_no, district_name, market_name, commodity, variety, grade, min_price,max_price, modal_price, date,state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"), row)
                #Commit the changes and close the database connection
                conn.commit()
                conn.close()


    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {str(e)}")
    except requests.exceptions.Timeout as e:
        print(f"Request Timeout: {str(e)}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {str(e)}")
    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--commodity", required=True)
    parser.add_argument("--start_date", required=True)
    parser.add_argument("--end_date", required=True)
    parser.add_argument("--time_agg", required=True)
    parser.add_argument("--states", required=True)

    args = parser.parse_args()

    # Call the scrape_agmarket function with the provided arguments
    scrape_agmarket(args.commodity, args.start_date, args.end_date, args.time_agg, args.states)


