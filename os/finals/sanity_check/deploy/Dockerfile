FROM ubuntu:22.04 AS app
FROM pwn.red/jail
COPY --from=app / /srv
COPY run.sh /srv/app/run
RUN chmod +x /srv/app/run
