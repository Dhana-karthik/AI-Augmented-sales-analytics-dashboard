import google.generativeai as genai 
import os 
from dotenv import load_dotenv


load_dotenv()

# configuring genai 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

SCHEMA ="""
Table: car_prices
Columns:
- vin(text)
- make(text)
- model(text)
- trim(text)
- body(text)
- transmission(text)
- vin(text)
- state(text)
- condition(int)
- odometer(int)
- color(text)
- interior(text)
- seller(text)
- mmr(int)
- sellingprice(int)
- saledate(datetime)
"""


def text_to_sql(user_query):
    prompt = f"""
  you are an SQLite professional. 

  Convert the following natural language query into SQL. 

  {SCHEMA}
  Rules: 
  - Only generate SELECT queries
  - Do not explain anything
  - Return only SQL query 
   Query: {user_query}
   """
    reponse = model.generate_content(prompt)
    return reponse.text.strip()
 
