FROM ubuntu
USER root

WORKDIR /app

RUN apt-get update && apt-get install -y python3.10
# RUN apt-get install -y python3.10
RUN apt-get install -y python3-distutils python3-pip python3-apt

COPY . .

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./log_centralizzato_server.py"]