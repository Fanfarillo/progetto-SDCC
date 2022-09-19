FROM ubuntu
USER root

WORKDIR /usr/local/
ADD InstallServer.sh .
ADD Consumer.py .

RUN apt-get update && apt-get install -y software-properties-common gcc && add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN pip install pika

EXPOSE 4369
CMD ["bash", "./InstallServer.sh"]
CMD ["python3", "./Consumer.py"]
