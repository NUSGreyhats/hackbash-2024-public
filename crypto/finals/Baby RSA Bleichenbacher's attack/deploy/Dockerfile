FROM ubuntu:20.04

RUN apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd

RUN apt-get install -y python3.8 python3-pip
RUN pip install pycryptodome

RUN useradd -m ctf

WORKDIR /home/ctf

COPY ./rsableichen.xinetd /etc/xinetd.d/rsableichen
COPY ./start.sh /start.sh
RUN echo "Blocked by xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./server.py /home/ctf/server.py

CMD ["/bin/sh", "/start.sh"]

EXPOSE 9999
