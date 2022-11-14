FROM ubuntu
USER root

WORKDIR /usr/local/
ADD InstallServer.sh .
ADD Producer.py .

RUN apt-get update && apt-get install -y software-properties-common gcc && add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN pip install pika

#Flush on stdout all the prints
ENV  PYTHONUNBUFFERED=1

CMD ["bash", "./InstallServer.sh"]
CMD ["python3", "./Producer.py"]
