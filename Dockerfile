FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN apk add bash

RUN pip install --upgrade pip setuptools \
    && pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x django.sh

ENTRYPOINT bash django.sh