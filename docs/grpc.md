i am using grpc to collect locations from mobile devices in the location producer service wich it keep listen on port `30005` 
```proto
syntax = "proto3";

message LocationMessage{
    int32 person_id = 1;
    string longitude = 2;
    string latitude = 3;
    string creation_time = 4;
}

service LocationService {
    rpc PushLocation(LocationMessage) returns (LocationMessage);
}
```

send a simple data by run the writer file in   `python modules/location_producer/writer.py`
```py
import grpc
import location_pb2
import location_pb2_grpc

print("Sending my Location ...")

channel = grpc.insecure_channel("localhost:30005")
stub = location_pb2_grpc.LocationServiceStub(channel)

myLocation = location_pb2.LocationMessage(
    person_id = 1,
    longitude = "126.5405",
    latitude = "126.5405",
    creation_time = "20120618 10:34:09 AM"
)
response = stub.PushLocation(myLocation)
print(response)
```