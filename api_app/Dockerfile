FROM python:3.12-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py /api_app.py
COPY schemas.py /api_app.py
COPY backend .
WORKDIR /api_app
CMD ["python", "main.py"]
EXPOSE 8080