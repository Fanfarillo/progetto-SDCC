FROM python:3.6.9
USER root

WORKDIR /usr/local/
ADD proto ./proto
ADD MicroServer.py .
RUN pip install grpcio grpcio-tools

EXPOSE 50051
CMD ["python", "./MicroServer.py"]
