FROM nginx:latest
RUN apt-get update && apt-get install -y nginx

FROM python:3.12-slim
COPY requirements.txt .
COPY main.py .
COPY api_app .
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN pip install -r requirements.txt
WORKDIR /
CMD ["python", "main.py"]
EXPOSE 8000
