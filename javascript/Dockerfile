FROM node:lts-bullseye

WORKDIR /code

COPY package.json package-lock.json /code/

RUN npm install

COPY . .
