import time
import json
import urllib.request
from kafka import KafkaProducer
from binance.client import Client
from binance import ThreadedWebsocketManager
from more_itertools import last

producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

topic_name = "depth20-btc"

#BASED ON: https://github.com/SpiralDevelopment/crypto-hft-data/blob/master/exchange_sockets/binance_websocket.py



def broadcast_kafka(msg): 
    stream = msg.get('stream', '')
    stream_parts = stream.split('@')
    data = msg.get('data')

    bids = data.get('bids', [])
    asks = data.get('asks', [])

    if len(bids) == 0 and len(asks) == 0:
        bids = data.get('b', [])
        asks = data.get('a', [])

    if len(bids) > 0 or len(asks) > 0:
        time_now = int(time.time())
        producer.send(topic_name, json.dumps({"time": time_now, "bids":bids, "asks": asks}))
        
def handle_message(msg):
        broadcast_kafka(msg)


client = Client('', '')


streams = ['btcbusd@depth20@100ms']

twm = ThreadedWebsocketManager()    
twm.start()
depth_stream_name = twm.start_multiplex_socket(callback=handle_message, streams=streams)
