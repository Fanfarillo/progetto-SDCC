python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/FroReg.proto
python3 -m grpc_tools.protoc -I. --python_out=./registration --grpc_python_out=./registration ./proto/FroReg.proto
