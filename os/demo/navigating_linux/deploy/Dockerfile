FROM ubuntu:22.04

RUN apt-get -y update
RUN apt-get install -y socat

ENV user XxLinuxProxX
RUN useradd -m $user
WORKDIR /home/$user

RUN mkdir flag_in_here
COPY README.txt /home/$user/flag_in_here
COPY bashrc /home/$user/.bashrc
COPY shell.sh /shell.sh
RUN chmod 555 /shell.sh

USER $user
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/shell.sh,stderr
