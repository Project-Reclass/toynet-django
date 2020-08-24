FROM ubuntu:latest

WORKDIR app

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get -y install python3.7
RUN apt-get -y install python3-pip
RUN apt-get -y install graphviz
RUN pip3 install diagrams==0.9.0

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY engine engine
RUN cd engine

EXPOSE 8000

CMD [ "python3", "/app/engine/manage.py", "runserver", "0.0.0.0:8000" ]
