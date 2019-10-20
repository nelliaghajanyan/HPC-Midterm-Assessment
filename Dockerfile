FROM hpc2019/ubuntu:twitter

COPY ./producer.py ./consumer.py /app/
WORKDIR /app

