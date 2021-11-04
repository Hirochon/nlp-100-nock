FROM python:3.10.0-buster
USER root

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less

COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY ./ /code/