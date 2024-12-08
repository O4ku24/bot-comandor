
FROM python:3.12-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY bot.py ./bot/bot.py
COPY main.py ./api_app
COPY shcemas.py ./api_app
WORKDIR /bot
CMD ["python", "bot.py"]
EXPOSE 3478