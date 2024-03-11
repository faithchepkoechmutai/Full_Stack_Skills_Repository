import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

# Task 1
def log_progress(log_points, log_file_path='code_log.txt'):
    with open(log_file_path, 'a') as log_file:
        for point in log_points:
            log_file.write(f"{point}\n")

# Task 2
def extract(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    df = pd.read_html(str(table))[0]
    return df

# Task 3
def transform(df, exchange_rate_path):
    exchange_rates = pd.read_csv(exchange_rate_path)
    df = pd.merge(df, exchange_rates, how='left', on='Currency')
    df['MC_GBP_Billion'] = df['MC_USD_Billion'] * df['GBP']
    df['MC_EUR_Billion'] = df['MC_USD_Billion'] * df['EUR']
    df['MC_INR_Billion'] = df['MC_USD_Billion'] * df['INR']
    df = df.round({'MC_GBP_Billion': 2, 'MC_EUR_Billion': 2, 'MC_INR_Billion': 2})
    return df

# Task 4
def load_to_csv(df, output_csv_path='./Largest_banks_data.csv'):
    df.to_csv(output_csv_path, index=False)

# Task 5
def load_to_db(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (Name TEXT, MC_USD_Billion REAL, MC_GBP_Billion REAL, MC_EUR_Billion REAL, MC_INR_Billion REAL)")
    conn.commit()
    df.to_sql(table_name, conn, index=False, if_exists='replace')
    conn.close()

# Task 6
def run_queries(db_name, table_name):
    conn = sqlite3.connect(db_name)
    query1 = f"SELECT * FROM {table_name}"
    query2 = f"SELECT Name, MC_USD_Billion FROM {table_name} WHERE MC_USD_Billion > 100"
    result1 = pd.read_sql(query1, conn)
    result2 = pd.read_sql(query2, conn)
    conn.close()
    return result1, result2

# Task 7
log_points = ["Task 1 started", "Task 1 completed", "Task 2 started", "Task 2 completed"]
log_progress(log_points)

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
data_frame = extract(url)

log_points = ["Task 3 started", "Task 3 completed"]
log_progress(log_points)

exchange_rate_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
transformed_df = transform(data_frame, exchange_rate_path)

log_points = ["Task 4 started", "Task 4 completed"]
log_progress(log_points)

output_csv_path = './Largest_banks_data.csv'
load_to_csv(transformed_df, output_csv_path)

log_points = ["Task 5 started", "Task 5 completed"]
log_progress(log_points)

db_name = "Banks.db"
table_name = "Largest_banks"
load_to_db(transformed_df, db_name, table_name)

log_points = ["Task 6 started", "Task 6 completed"]
log_progress(log_points)

query_result1, query_result2 = run_queries(db_name, table_name)

log_points = ["Task 7 started", "Task 7 completed"]
log_progress(log_points)