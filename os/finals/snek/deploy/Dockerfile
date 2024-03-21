FROM ubuntu:22.04

RUN apt-get update && apt-get install -y unzip socat python3 && rm -rf /var/lib/apt/lists/*

COPY snek.txt /snek.txt
RUN chown root /snek.txt
RUN chmod 600 /snek.txt

COPY flag.txt /flag.txt
RUN chown root /flag.txt
RUN chmod 600 /flag.txt

COPY hello.py /.hello.py
RUN chown root /.hello.py
RUN chmod o+rx /.hello.py

COPY hello /
RUN chown root /hello
RUN chmod o+rx /hello
RUN chmod u+s /hello

COPY deployer.py /
RUN chmod +x /deployer.py

COPY passwd /
RUN chmod 644 /passwd

COPY group /
RUN chmod 644 /group

COPY shadow /
RUN chmod 640 /shadow

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/deployer.py,pty,stderr,setsid,sigint,sane
