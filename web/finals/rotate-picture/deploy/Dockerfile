FROM php:8.1-apache

COPY flag readflag.c /

RUN apt-get update && apt-get install -y gcc

RUN apt-get install -y libpng-dev libjpeg-dev libfreetype6-dev && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install -j$(nproc) gd

RUN gcc -o /readflag /readflag.c && \
    rm /readflag.c && \
    chmod 4755 /readflag && \ 
    chmod 400 /flag

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer
WORKDIR /var/www/html
COPY src/composer.json /var/www/html/composer.json
RUN apt-get install -y git unzip && composer install

RUN chown -R root:root /var/www/html/ && \
    chmod -R 555 /var/www/html/ && \
    mkdir /var/www/html/uploads && \
    chown -R www-data:www-data /var/www/html/uploads && \
    chmod -R 755 /var/www/html/uploads

COPY src/ /var/www/html/