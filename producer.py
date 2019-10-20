from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import time
import tweepy as tw
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class StdOutListener(StreamListener):

    def __init__(self):
        pass
    def on_data(self, data):
        try:
	    # uncomment to see the data streaming into kafka
            # print(loads(data)['text'])
            producer.send('topic', loads(data)['text'])
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)
        
class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, hash_tag_list):
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)

not_connected = True
while not_connected:
    try:
        producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
	                 value_serializer=lambda x: 
	                 dumps(x).encode('utf-8'))
        not_connected=False
    except Exception as e:
        continue

consumer_key= '2GMpPxAfvRpCw17D9O7U44rm8'
consumer_secret= '352VDqOjbVufblsGGGJdInAnjIJR3sBEznQ0kVDStx0dGSEish'
access_token= '1617684481-LcMk6aBlKqltK2Jj0323UbFHvQEYzIwbAfQIDVW'
access_token_secret= '33RgFACthNzXipcUABqI5tdKV8JLNpFArDynHMbiuuXOh'

hash_tag_list = ["#trump"]

twitter_streamer = TwitterStreamer()
twitter_streamer.stream_tweets(hash_tag_list)

