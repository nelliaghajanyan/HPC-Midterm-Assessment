FROM ubuntu:hpc

COPY ./producer.py ./consumer.py /app/
WORKDIR /app

