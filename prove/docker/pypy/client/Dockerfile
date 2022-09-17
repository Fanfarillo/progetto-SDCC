FROM python:3.6.9
USER root

WORKDIR /usr/local/
ADD proto ./proto
ADD MicroClient.py .
RUN pip install grpcio grpcio-tools

EXPOSE 50052
CMD ["python", "./MicroClient.py"]
