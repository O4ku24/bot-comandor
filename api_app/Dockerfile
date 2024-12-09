FROM python:3.12-slim
COPY requirements.txt .
COPY main.py .
COPY backend.py .
COPY database.py .
COPY schemas.py .
COPY templates .
RUN pip install -r requirements.txt
FROM nginx:latest
COPY index.html /usr/share/nginx/html/
COPY 1.jpg /usr/share/nginx/html/
RUN apt-get update && apt-get install -y nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
WORKDIR /
CMD ["python", "main.py"]
EXPOSE 8080
