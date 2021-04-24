FROM nginx:latest
LABEL key="Edney Ferreira"


COPY nginx/config/nginx.conf /etc/nginx/nginx.conf


EXPOSE 80 443

ENTRYPOINT ["nginx"]

CMD ["-g", "daemon off;"]
