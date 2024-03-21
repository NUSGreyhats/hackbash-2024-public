FROM ubuntu:22.04

RUN apt-get -y update
RUN apt-get install -y socat python3

COPY challenge /challenge
COPY challenge.py /challenge.py
COPY flag.txt /flag.txt
RUN chmod 555 /challenge.py
RUN chmod 555 /challenge

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challenge.py,stderr
