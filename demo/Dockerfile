FROM node:lts-alpine AS build-frontend

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine
COPY --from=build-frontend /app/dist/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
