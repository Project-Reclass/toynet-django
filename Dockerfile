FROM python:3.8-slim

WORKDIR app

RUN apt-get update && apt-get install -y \
    graphviz \ 
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY engine engine
RUN cd engine

EXPOSE 8000

CMD [ "python", "/app/engine/manage.py", "runserver", "0.0.0.0:8000" ]
