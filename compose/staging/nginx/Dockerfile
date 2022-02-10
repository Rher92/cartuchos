FROM nginx:1.21.6-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/staging/nginx/nginx.conf /etc/nginx/conf.d