FROM node:latest
LABEL key="Edney Ferreira"

RUN npm install --global npm@7.10.0 

USER root
WORKDIR /var/www


COPY ./front /var/www
RUN npm cache clean --force 
RUN npm install
RUN npm install  -g --silent --force react-scripts@4.0.3
RUN npm install axios --force
RUN npm install --save --force react-score-indicator
RUN npm install --force react-bootstrap bootstrap
RUN npm install --force styled-components 


CMD ["npm" ,"start"]

EXPOSE 3000
