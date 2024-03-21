FROM ubuntu:latest as builder
WORKDIR /app

COPY git.zip .
RUN apt-get update
RUN apt-get install unzip
RUN unzip git.zip

FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY ctf-challenge.conf /etc/nginx/conf.d/ctf-challenge.conf

COPY . /var/www/html/
WORKDIR /var/www/html/
COPY --from=builder /app/.git /var/www/html/.git
EXPOSE 55503

