FROM ubuntu:20.04

RUN apt-get update -y && apt-get install -y python3-pip python3-dev vim

COPY ./requirements.txt /flask-api/requirements.txt

WORKDIR /flask-api

RUN pip3 install -r requirements.txt

COPY . /flask-api

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "8080" ]