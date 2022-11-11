FROM ubuntu
USER root

WORKDIR /app
COPY . .
COPY ./credentials /root/.aws/

RUN apt-get update && apt-get install -y python3.10
# RUN apt-get install -y python3.10
RUN apt-get install -y python3-distutils python3-pip python3-apt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 50051
CMD ["python3", "./registration.py"]
