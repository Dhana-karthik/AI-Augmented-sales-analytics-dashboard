import sqlite3
import pandas as pd



DB_NAME = "sales.db"
CSV_FILE = "car_prices.csv"

def load_csv_to_db():

    df = pd.read_csv(CSV_FILE)
    
    #connecting to SQLite
    connection =  sqlite3.connect(DB_NAME)
    
    #write to table 
    df.to_sql("sales",connection, if_exists="replace", index = False)
    
    connection.close()
    print("csv loaded into sqlite")

def run_query(query):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    cursor.execute(query)
    rows = cursor.fetchall()

    connection.close()
    return rows

