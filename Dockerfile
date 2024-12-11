
FROM python:3.12-slim
COPY requirements.txt .
COPY main.py .
COPY backend .

RUN pip install -r requirements.txt
WORKDIR /
CMD ["python", "main.py"]
EXPOSE 8000
