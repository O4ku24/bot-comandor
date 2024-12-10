FROM nginx:latest
COPY default /etc/nginx/sites-available/default
RUN apt-get -y update && apt-get -y install nginx

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
