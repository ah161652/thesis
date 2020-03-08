FROM ubuntu:18.04

RUN yes | apt-get update
RUN yes | apt-get -y upgrade

RUN yes | apt-get install python
RUN yes | apt-get install python-pip
RUN yes | pip install request
RUN yes | pip install pycrypto

RUN touch /root/secret.c
RUN touch /root/secret.pdf
RUN touch /home/secret.c
RUN touch /home/secret.pdf

COPY GonnaCry /root
