python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/FroReg.proto
python3 -m grpc_tools.protoc -I. --python_out=./registration --grpc_python_out=./registration ./proto/FroReg.proto

python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/FroMan.proto
python3 -m grpc_tools.protoc -I. --python_out=./management --grpc_python_out=./management ./proto/FroMan.proto

python3 -m grpc_tools.protoc -I. --python_out=./management --grpc_python_out=./management ./proto/BooMan.proto
python3 -m grpc_tools.protoc -I. --python_out=./booking --grpc_python_out=./booking ./proto/BooMan.proto
