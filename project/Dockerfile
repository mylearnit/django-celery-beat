# pull official base image
FROM python:3.9.5

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install supervisord
RUN apt-get update && apt-get install -y supervisor

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

COPY ./gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf
COPY ./supervisor_app.conf /etc/supervisor/conf.d/supervisor_app.conf
COPY ./supervisord.conf /etc/supervisor/supervisord.conf


# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
