FROM ubuntu:22.04

ENV user player

RUN apt-get -y update
RUN apt-get install -y socat

RUN useradd -m $user
WORKDIR /home/$user

# runner script to spawn new user
COPY lore.txt /home/$user/lore.txt
RUN chmod 444 /home/$user/lore.txt

COPY flag.txt /flag.txt
RUN chmod 400 /flag.txt

COPY time /usr/bin/time
RUN chmod u+s /usr/bin/time


USER $user

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/bin/bash,stderr
