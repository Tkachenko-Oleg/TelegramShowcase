FROM python:3.10

WORKDIR /TelegramBot

COPY /app ./app/
COPY .env .
COPY requirements.txt .
COPY run.sh .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["bash", "run.sh"]
