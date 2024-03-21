FROM php:8.1-apache

COPY .  /var/www/html/
COPY apache2.conf /etc/apache2/
RUN chmod +r /etc/apache2/apache2.conf

RUN chown -R root:root /var/www/
RUN chmod -R 755 /var/www/

RUN sed -i "s/Listen 80/Listen 8080/" /etc/apache2/ports.conf 

RUN echo "flag{h0w_d1d_y0u_s33_th1s?}" >> /etc/passwd

USER www-data
