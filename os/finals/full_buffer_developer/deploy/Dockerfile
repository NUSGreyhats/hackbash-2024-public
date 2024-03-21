FROM pwn.red/jail
COPY --from=ubuntu:22.04 / /srv

COPY flag.txt /srv/app/flag.txt
COPY full_buffer_developer /srv/app/run

RUN chmod +x /srv/app/run
