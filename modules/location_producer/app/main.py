import time
import datetime
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from json import dumps
from kafka import KafkaProducer

TOPIC_NAME = "location"
KAFKA_SERVER = 'my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER],value_serializer=lambda k:dumps(k).encode('utf-8'))

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def PushLocation(self, request, context):
        location_obj = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude,
            "creation_time": request.creation_time
        }
        print(location_obj)
        print("push in enquee...")
        producer.send(TOPIC_NAME, location_obj)
        producer.flush()
        print("Don")
        return location_pb2.LocationMessage(**location_obj)
    

# Intitialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on Port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)