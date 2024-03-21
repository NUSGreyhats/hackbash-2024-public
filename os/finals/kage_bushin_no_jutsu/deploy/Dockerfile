FROM ubuntu:22.04

RUN apt-get update && apt-get install -y unzip socat && rm -rf /var/lib/apt/lists/*

ENV user player
RUN useradd -m $user
WORKDIR /home/$user

COPY ./chall.zip /tmp
RUN unzip /tmp/chall.zip -d /home/$user
RUN rm /tmp/chall.zip

RUN rm /home/player/.bash_logout
RUN rm /home/player/.bashrc
RUN rm /home/player/.profile

USER $user
CMD socat TCP-LISTEN:5000,reuseaddr,fork exec:"bash -i",pty,stderr,setsid,sigint,sane
