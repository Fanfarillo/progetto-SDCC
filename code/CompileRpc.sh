python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Registration.proto
python3 -m grpc_tools.protoc -I. --python_out=./registration --grpc_python_out=./registration ./proto/Registration.proto

python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Managment.proto
python3 -m grpc_tools.protoc -I. --python_out=./management --grpc_python_out=./management ./proto/Managment.proto
python3 -m grpc_tools.protoc -I. --python_out=./booking --grpc_python_out=./booking ./proto/Managment.proto

python3 -m grpc_tools.protoc -I. --python_out=./management --grpc_python_out=./management ./proto/Booking.proto
python3 -m grpc_tools.protoc -I. --python_out=./booking --grpc_python_out=./booking ./proto/Booking.proto

python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Booking.proto
