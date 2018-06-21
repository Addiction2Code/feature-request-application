FROM tiangolo/uwsgi-nginx-flask:python3.6

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -qq update
RUN apt-get -qq install curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get -qq update
RUN apt-get -qq install nodejs

RUN npm install -g bower

ADD requirements.txt /tmp/requirements.txt 

RUN pip install -r /tmp/requirements.txt

COPY . /app

ENV STATIC_PATH /app/app/static

WORKDIR /app

RUN python db_create.py

WORKDIR /app/app/static

RUN bower install --allow-root

WORKDIR /app

EXPOSE 8000
