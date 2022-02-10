FROM node:lts-alpine

ENV PATH /app/node_modules/.bin:$PATH

COPY ./frontend .

RUN npm install @vue/cli@4.5.13 -g
RUN npm install -g http-server
RUN npm install

WORKDIR /app

RUN npm run build

CMD [ "http-server", "dist" ]
