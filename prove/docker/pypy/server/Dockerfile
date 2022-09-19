FROM ubuntu
USER root

WORKDIR /usr/local/
ADD proto ./proto
ADD MicroServer.py .

RUN apt-get update && apt-get install -y software-properties-common gcc && add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN pip install grpcio grpcio-tools

EXPOSE 50051
CMD ["python3", "./MicroServer.py"]
