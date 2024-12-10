FROM nginx:latest
RUN apt-get update && apt-get install -y nginx

FROM python:3.12-slim
COPY requirements.txt api_app/
COPY main.py api_app/
COPY backend.py api_app/
COPY database.py api_app/
COPY schemas.py api_app/
COPY templates api_app/
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN pip install -r requirements.txt
WORKDIR /
CMD ["python", "main.py"]
EXPOSE 8000
