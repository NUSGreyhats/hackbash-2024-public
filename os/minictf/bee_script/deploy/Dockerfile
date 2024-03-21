FROM pwn.red/jail
COPY --from=ubuntu / /srv
# setup the binary to r
COPY bee_movie_script /srv/app/bee_movie_script
RUN ln -s /bin/sh /srv/app/run
