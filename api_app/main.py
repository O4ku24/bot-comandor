import uvicorn
from fastapi import FastAPI, Request
import pandas as pd

from backend.backend import get_data_db_period, seve_data_db, get_all_data
from api_app.schemas import Sale, DatePeriod

app = FastAPI(
    title="Bot Saler",
    version="0.0.1"
)

@app.get('/sales/')
def get_all(request:Request):

    file = get_all_data()
    data = {}
    if file['status'] == '200 OK':
        data['status'] = file['status']
        df = pd.read_excel(file['file'])
        for index, row in df.iterrows():
            data[index+1] = {'title' : row['title'], 
                            'price' : row['price'], 
                            'date' : row['date']}
        
        return data
    
@app.post('/sales/')
def get_period(request:Request, period:DatePeriod):

    file = get_data_db_period(period.start, period.end)
    data = {}
    if file['status'] == '200 OK':
        data['status'] = file['status']
        data['period'] = file['period']
        df = pd.read_excel(file['file'])
        for index, row in df.iterrows():
            data[index+1] = {'title' : row['title'], 
                            'price' : row['price'], 
                            'date' : row['date']}
        
        return data



@app.post('/add/')
def add_sales(request:Request, sele:Sale):

    status = seve_data_db(sele.title, sele.price)
    return status


if __name__ == '__main__':
    uvicorn.run(app, port=5050)