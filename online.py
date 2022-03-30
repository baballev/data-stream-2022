import river
import kafka
from kafka import KafkaConsumer
import numpy as np
from river import preprocessing
import json

topic_name = "depth20-btc"

consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092")
price_norm_factor = 45000.0
qtity_norm_factor = 5.0

model = river.time_series.SNARIMAX(p=0, d=0, q=0, m=10, sp=3, sq=6, regressor=(preprocessing.StandardScaler() | river.linear_model.LinearRegression(intercept_init=110, optimizer=river.optim.SGD(0.01), intercept_lr=0.3)))


i = 0
y = np.zeros(4, dtype=float)

for message in consumer:
    json_obj = json.loads(message.value)
    time = json_obj["time"]
    bids = json_obj["bids"]
    asks = json_obj["asks"]
    print(json_obj)
    l = [(float(ask[0]) - price_norm_factor)/price_norm_factor for ask in asks] + [(float(ask[1])-qtity_norm_factor)/qtity_norm_factor for ask in asks] + [(float(bid[0])-price_norm_factor)/price_norm_factor for bid in bids] + [(float(bid[1])-qtity_norm_factor)/qtity_norm_factor for bid in bids]
    tensor = np.array(l, dtype=float)

    if i == 0:
        pass
    else:
        pass




