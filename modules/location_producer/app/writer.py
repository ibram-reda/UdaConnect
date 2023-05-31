import datetime

import grpc
import location_pb2
import location_pb2_grpc


print("Sending my Location ...")

channel = grpc.insecure_channel("localhost:30005")
stub = location_pb2_grpc.LocationServiceStub(channel)

myLocation = location_pb2.LocationMessage(
    person_id = 1,
    longitude = "it works fine!",
    latitude = "126.5405",
    creation_time = "2002-2-2:24:0"
)

response = stub.PushLocation(myLocation)

print(response)