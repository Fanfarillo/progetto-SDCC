python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Registration.proto
python3 -m grpc_tools.protoc -I. --python_out=./registration --grpc_python_out=./registration ./proto/Registration.proto
python3 -m grpc_tools.protoc -I. --python_out=./logging --grpc_python_out=./logging ./proto/Registration.proto

python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Managment.proto
python3 -m grpc_tools.protoc -I. --python_out=./management --grpc_python_out=./management ./proto/Managment.proto
python3 -m grpc_tools.protoc -I. --python_out=./booking --grpc_python_out=./booking ./proto/Managment.proto
python3 -m grpc_tools.protoc -I. --python_out=./logging --grpc_python_out=./logging ./proto/Managment.proto

python3 -m grpc_tools.protoc -I. --python_out=./management --grpc_python_out=./management ./proto/Booking.proto
python3 -m grpc_tools.protoc -I. --python_out=./booking --grpc_python_out=./booking ./proto/Booking.proto
python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Booking.proto
python3 -m grpc_tools.protoc -I. --python_out=./logging --grpc_python_out=./logging ./proto/Booking.proto

python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Payment.proto
python3 -m grpc_tools.protoc -I. --python_out=./payment --grpc_python_out=./payment ./proto/Payment.proto
python3 -m grpc_tools.protoc -I. --python_out=./logging --grpc_python_out=./logging ./proto/Payment.proto

python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Suggestions.proto
python3 -m grpc_tools.protoc -I. --python_out=./booking --grpc_python_out=./booking ./proto/Suggestions.proto
python3 -m grpc_tools.protoc -I. --python_out=./logging --grpc_python_out=./logging ./proto/Suggestions.proto

python3 -m grpc_tools.protoc -I. --python_out=./discovery --grpc_python_out=./discovery ./proto/Discovery.proto
python3 -m grpc_tools.protoc -I. --python_out=./frontend --grpc_python_out=./frontend ./proto/Discovery.proto
python3 -m grpc_tools.protoc -I. --python_out=./booking --grpc_python_out=./booking ./proto/Discovery.proto
python3 -m grpc_tools.protoc -I. --python_out=./management --grpc_python_out=./management ./proto/Discovery.proto
python3 -m grpc_tools.protoc -I. --python_out=./registration --grpc_python_out=./registration ./proto/Discovery.proto
python3 -m grpc_tools.protoc -I. --python_out=./logging --grpc_python_out=./logging ./proto/Discovery.proto
