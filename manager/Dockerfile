FROM php:7.2-apache

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

COPY ./src /var/www/html
RUN chmod -R 755 /var/www/html

COPY apache-config.conf /etc/apache2/sites-enabled/000-default.conf
CMD /usr/sbin/apache2ctl -D FOREGROUND
