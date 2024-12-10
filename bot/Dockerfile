FROM python:3.12-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY bot.py /bot/bot.py
WORKDIR /bot
CMD ["python", "bot.py"]
EXPOSE 5000