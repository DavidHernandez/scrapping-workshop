FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

