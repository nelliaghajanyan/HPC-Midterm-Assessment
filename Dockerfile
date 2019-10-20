FROM ubuntu:twitter

COPY ./producer.py ./consumer.py /app/
WORKDIR /app

