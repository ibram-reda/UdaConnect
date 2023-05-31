from kafka import KafkaConsumer
from services import LocationService
from datetime import datetime
import json
import logging

TOPIC_NAME = "location"
KAFKA_SERVER = 'my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'

consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=[KAFKA_SERVER])
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("location Consumer")

for message in consumer:
    try:
        location = json.loads(message.value.decode("utf-8"))
        logger.info("reseving -----------------------------------------")
        logger.info(location)
        LocationService.create(location)
        logger.info(" yahoooooOOooOoOow saved into database!")
    except Exception as err:
        logger.error(f"--Unexpected {err}, {type(err)}")