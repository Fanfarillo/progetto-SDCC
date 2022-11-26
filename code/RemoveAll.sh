docker-compose stop
docker-compose down --remove-orphans
docker rmi code_booking:latest
docker rmi code_frontend:latest
docker rmi code_management:latest
docker rmi code_payment:latest
docker rmi code_registration:latest
docker rmi code_suggestions:latest
docker rmi code_discovery:latest
docker rmi code_logging:latest
docker rmi rabbitmq:3.6-management-alpine
docker system prune
