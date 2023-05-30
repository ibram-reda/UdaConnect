## micro services
- I take out persons and Connections URLs to it's microservices which communicate through Restful API to make it easy to communicate with the front end (Restful is easy to **maintenance**)

- I have decided to collect location from users through gRPC to reduce the load on users network because we keep tracking location (smaller data will transfer through gRPC, then it's more **efficient**)

- due to there is a lot of users send their location in same time, I have decided to use Kafka to minimize data lose to the high load (Kafka will provide high **reliability**)