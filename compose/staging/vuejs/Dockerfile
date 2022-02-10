FROM node:lts-alpine as build-stage

ENV PATH /app/node_modules/.bin:$PATH

WORKDIR /app

COPY ./frontend .

RUN npm install @vue/cli@4.5.13 -g
RUN npm install

RUN npm run build

FROM nginx:1.16.0-alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/staging/nginx/nginx.conf /etc/nginx/conf.d
CMD ["nginx", "-g", "daemon off;"]