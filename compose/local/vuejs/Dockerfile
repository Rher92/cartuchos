FROM node:lts-alpine

ENV PATH /app/node_modules/.bin:$PATH

COPY ./frontend/package.json .
COPY ./frontend/package-lock.json .

RUN npm install @vue/cli@4.5.13 -g

RUN npm install

WORKDIR /app

CMD ["npm", "run", "serve"]