FROM python:3
LABEL key="Edney Ferreira"

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y libdbus-1-dev libdbus-glib-1-dev

COPY ./python/requirements.txt ./
RUN pip install --user numpy scipy pymongo  pandas  flask flask-cors gevent scikit-learn
COPY ./python .
WORKDIR /usr/src/app/python/api


CMD [ "python", "routes.py" ]

EXPOSE 5000