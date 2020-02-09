### [ Build stage ]=====================================

FROM node:12.2.0-alpine as build

WORKDIR /app
COPY . /app

RUN npm install --silent
RUN npm run build

### [ Run stage ]=====================================

FROM nginx:1.16.0-alpine as run

LABEL maintainer "Alen Kocaj <alen.kocaj@posteo.at>"

RUN mkdir /etc/nginx/html

COPY --from=build /app/build /etc/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf 

CMD ["nginx", "-g", "daemon off;"]