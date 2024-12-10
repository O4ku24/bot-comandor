FROM python:3.12-slim
COPY requirements.txt .
COPY main.py .
COPY backend.py .
COPY database.py .
COPY schemas.py .
COPY templates .
RUN pip install -r requirements.txt

WORKDIR /
CMD ["python", "main.py"]
EXPOSE 8000
