systemctl stop rabbitmq-server
docker-compose up --build --scale discovery=2 --scale suggestions=2
