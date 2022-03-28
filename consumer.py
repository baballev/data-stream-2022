import time
import json
from kafka import KafkaConsumer
import numpy as np

topic_name = "depth20-btc"

consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092")

#model = # TODO IMPORT Online MODEL


price_norm_factor = 45000.0
qtity_norm_factor = 5.0


for message in consumer:
    json_obj = json.loads(message.value)
    time = json_obj["time"]
    bids = json_obj["bids"]
    asks = json_obj["asks"]
    l = [(float(ask[0]) - price_norm_factor)/price_norm_factor for ask in asks] + [(float(ask[1])-qtity_norm_factor)/qtity_norm_factor for ask in asks] + [(float(bid[0])-price_norm_factor)/price_norm_factor for bid in bids] + [(float(bid[1])-qtity_norm_factor)/qtity_norm_factor for bid in bids]
    tensor = np.array(l, dtype=float)


    # Tensor ready to use input, normalized

    #Make online prediction with streaming model


