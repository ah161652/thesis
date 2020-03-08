FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install python
RUN apt-get install python-pip
RUN pip install request
RUN pip install pycrypto

RUN touch /root/secret.c
RUN touch /root/secret.pdf
RUN touch /home/secret.c
RUN touch /home/secret.pdf

COPY thesis /root
