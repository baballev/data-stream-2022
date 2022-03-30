import time
import json
from kafka import KafkaConsumer
import numpy as np

topic_name = "depth20-btc"

consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092")

#model = # TODO IMPORT Online MODEL


price_norm_factor = 45000.0 # This approximately bitcoin price. We normalize and center around 0 using this number for the price


for message in consumer: # Currently, ingest-data send the orderbooko depth 20 every 100 ms i.e 10 times per second
    json_obj = json.loads(message.value)
    time = json_obj["time"]
    bids = json_obj["bids"]
    asks = json_obj["asks"]
    l = [(float(ask[0]) - price_norm_factor)/price_norm_factor for ask in asks] + [float(ask[1]) for ask in asks] + [(float(bid[0])-price_norm_factor)/price_norm_factor for bid in bids] + [float(bid[1]) for bid in bids]
    tensor = np.array(l, dtype=float)


    # Tensor ready to use input, normalized

    #Make online prediction with streaming model


