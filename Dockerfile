FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN apt-get update && \
    apt-get install -y postgresql-client

WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app .
