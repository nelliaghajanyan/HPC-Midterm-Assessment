from kafka import KafkaConsumer
from json import loads
import time
not_connected = True
while not_connected:
    try:
        consumer = KafkaConsumer(
    'topic',
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

        not_connected=False
    except Exception as e:
        continue


current_time = time.time()
time_interval = 10 # in seconds
interval_words = [0]

for i in consumer:
   
    t = time.time()
    if t - current_time < time_interval:
        interval_words[-1] += len(i.value.split())
    else:
        print('Number of words', interval_words[-1])        
        interval_words.append(0)
        current_time = t
