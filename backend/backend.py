
from database import Connect
import datetime
import pandas as pd

def seve_data_db(title:str, price:float):
    print('seve_date_db')
    date = round(datetime.datetime.now().timestamp())
    connect = Connect('database.db')
    connect.insert(title, price, date)
    return {'status' : '200 OK'}

def get_data_db_period(start_period:str, end_period:str):
    start_period_total = round(datetime.datetime.strptime(start_period, '%d-%m-%Y, %H:%M').timestamp())
    end_period_total = round(datetime.datetime.strptime(end_period, '%d-%m-%Y, %H:%M').timestamp())
    connect = Connect('database.db')
    conn = connect.connection
    df = pd.read_sql(f'select * from Sales WHERE {end_period_total} >= date AND date >= {start_period_total}', conn)
    for i in range(len(df['date'])):
        df['date'][i] = datetime.datetime.fromtimestamp(df['date'][i]).strftime("%A, %B %d, %Y %I:%M:%S")
    
    df.to_excel('result.xlsx', index=False)
    file = open('result.xlsx', 'rb')
    
    
    return {
        'status' : '200 OK',
        'period' : f'С {start_period} по {end_period}',
        'file' : file
    }

def get_all_data():
    
    connect = Connect('database.db')
    conn = connect.connection
    df = pd.read_sql(f'select * from Sales', conn)
    for i in range(len(df['date'])):
        df['date'][i] = datetime.datetime.fromtimestamp(df['date'][i]).strftime("%A, %B %d, %Y %I:%M:%S")
    
    df.to_excel('result.xlsx', index=False)
    file = open('result.xlsx', 'rb')
    return {
        'status' : '200 OK',
        'file' : file
    }
