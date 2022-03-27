import time
import json
import urllib.request
from kafka import KafkaProducer
from binance.client import Client


producer = KafkaProducer(bootstrap_servers="localhost:9092")

topic_name = "velib-stations"

with open("./API_KEY", 'r') as f:
    API_KEY = f.readline()


uri = "wss://stream.binance.com:9443" 

while True:
    time.sleep(1)