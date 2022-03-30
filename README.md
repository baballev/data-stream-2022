# data-stream-2022
Projet data stream 2022


## Installation

After cloning the repo, run
```
pip install -r requirements.txt
```
to install the required packages.

Then, start kafka with the following commands:
```
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ bin/kafka-server-start.sh config/server.properties
```

You can then create the topic when running for the first time:
```
$ bin/kafka-topics.sh --create --topic depth20-btc --bootstrap-server localhost:9092
```

After that, running 

```
python ingest-data.py
```
will get the data stream from binance API and write it to the topic which is read by `consumer.py`
