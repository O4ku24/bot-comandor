
FROM python:3.12-slim

COPY requirements.txt .
COPY main.py .
COPY backend .

RUN pip install -r requirements.txt
<<<<<<<< HEAD:backend/Dockerfile

COPY main.py .
COPY backend .

CMD ["python", "main.py"]
EXPOSE 3000
========
WORKDIR /
CMD ["python", "main.py"]
EXPOSE 8000
>>>>>>>> 5f55e755dfcbeb0ff5806aa207ac19bd7da7254a:Dockerfile
