
FROM python:3.12-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY backend .

CMD ["python", "main.py"]
EXPOSE 3000
