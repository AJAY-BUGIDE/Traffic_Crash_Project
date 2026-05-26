#Libraries
import pandas as pd
from sqlalchemy import create_engine

#Loading dataset
filepath = "D:\\Ajay\\Traffic_Crash_Project\\Dataset\\Traffic_CrashesData.csv"

# load csv
df = pd.read_csv(filepath)

#Creating connection to database
engine = create_engine('mysql+pymysql://root:2193@localhost:3306/traffic_crash_db')

#Load data into database
df.to_sql('traffic_crashes', 
          con=engine, 
          if_exists='replace', 
          index=False)

print("Data Loaded Successfully")