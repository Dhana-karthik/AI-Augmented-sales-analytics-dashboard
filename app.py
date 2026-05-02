
# connecting to sqllite3
from sql import load_csv_to_db, run_query
import google.generativeai as genai
from llm import text_to_sql
load_csv_to_db()

#Queries 
query = "SELECT * FROM car_prices"
results = run_query(query)

for row in results:
    print(row)

