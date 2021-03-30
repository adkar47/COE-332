FROM ubuntu:latest

ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8
RUN apt-get update -y &&\
    apt-get install -y python3-dev python3-pip build-essential

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
