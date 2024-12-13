FROM python:3.12-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5454

CMD ["python", "main.py"]
