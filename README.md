# kafka-cluster
Kafka-ZK cluster with docker-compose (local or remote)

## How to use:
Edit .env file to set your current ip adress, or `127.0.0.1` if you want to deploy locally

Install docker and docker-compose, and run:

```shell
docker-compose up --build
```

to fire it up. And run:

```shell
docker-compose down
```

to stop de server.

## Test
For testing the stack, download [Kafka binaries](https://kafka.apache.org/downloads) and save to `/opt/kafka`.  Then, go to `/opt/kafka/bin` folder and create a topic for testing:

```shell
kafka-topics --create --bootstrap-server <<ip-adress-in-.env-file>>:9092 --replication-factor 1 --partitions 1 --topic numtest
```

Now you can test everything with the simple `producer.py` and `consumer.py`in the root folder of ths project. First of all install requirements:


```shell
pip install -r requirements.txt
```

And finally, run the following commands in to diferent terminals:

```shell
python producer.py

python consumer.py
```

You should see the output messages.
