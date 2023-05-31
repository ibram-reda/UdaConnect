instruction to use grpc-tools to generate required files
```cmd
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto
```