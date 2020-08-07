FROM nginx:1.19

COPY app /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf