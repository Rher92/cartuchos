FROM node:lts-alpine

ENV PATH /app/node_modules/.bin:$PATH

WORKDIR /app

COPY ./frontend .

RUN npm install @vue/cli@4.5.13 -g
RUN npm install -g http-server
RUN npm install


RUN npm run build

CMD [ "http-server", "dist" ]
