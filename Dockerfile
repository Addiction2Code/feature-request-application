FROM tiangolo/uwsgi-nginx-flask:python3.6

ADD requirements.txt /tmp/requirements.txt 

RUN pip install -r /tmp/requirements.txt

COPY . /app

ENV STATIC_PATH /app/app/static

WORKDIR /app

RUN python db_create.py

EXPOSE 8000
