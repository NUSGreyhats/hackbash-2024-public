FROM pwn.red/jail
COPY --from=ubuntu / /srv

COPY ./directory /srv/app/start_here

RUN ln -s /bin/sh /srv/app/run
