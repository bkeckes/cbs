# FROM nginx:perl

# COPY ./root_nginx.conf /etc/nginx/nginx.conf
# COPY ./nginx.conf /etc/nginx/conf.d/default.conf
# COPY ./nginx_conf /etc/nginx

FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d/*
COPY services/* /etc/nginx/conf.d/

COPY index.html /etc/nginx/html/
RUN chmod 755 -R /etc/nginx/html/

EXPOSE 80
