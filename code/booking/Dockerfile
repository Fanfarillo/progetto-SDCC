FROM ubuntu
USER root

WORKDIR /app

RUN apt-get update && apt-get install -y python3.10
# RUN apt-get install -y python3.10
RUN apt-get install -y python3-distutils python3-pip python3-apt

COPY . .
COPY ./credentials /root/.aws/

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 50053

#Flush on stdout all the prints
ENV  PYTHONUNBUFFERED=1

CMD ["bash", "./InstallMqServer.sh"]
CMD ["python3", "./booking.py"]
