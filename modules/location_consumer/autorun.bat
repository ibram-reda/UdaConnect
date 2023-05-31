docker build -t ibramreda/udaconnect-location-consumer:latest .
docker push ibramreda/udaconnect-location-consumer:latest
kubectl delete -f ..\..\deployment\udaconnect-location-consumer.yml
kubectl apply -f ..\..\deployment\udaconnect-location-consumer.yml
kubectl get pods