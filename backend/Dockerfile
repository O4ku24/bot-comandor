
FROM python:3.12-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY backend.py .
COPY database.py . 
COPY schemas.py .


CMD ["python", "main.py"]
EXPOSE 8000
