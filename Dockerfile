FROM python:3.8-alpine
MAINTAINER TREV TECH DEVELOPER LIMITED.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app
RUN adduser -D user

USER user