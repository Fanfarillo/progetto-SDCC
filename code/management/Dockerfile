FROM ubuntu
USER root

WORKDIR /app

RUN apt-get update && apt-get install -y python3.10
# RUN apt-get install -y python3.10
RUN apt-get install -y python3-distutils python3-pip python3-apt

COPY . .
COPY ./credentials /root/.aws/

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 50052
CMD ["python3", "./managment.py"]
