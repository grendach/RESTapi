FROM ubuntu:latest
MAINTAINER Dmytro Grendach "grendach@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3 build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT ["python3", "/app/server.py"]
