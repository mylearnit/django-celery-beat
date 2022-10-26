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


COPY ./start_gunicorn /start_gunicorn
ARG CACHEBUST=1
RUN sed -i 's/\r$//g' /start_gunicorn
RUN chmod +x /start_gunicorn

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# run supervisord
# CMD ["/usr/bin/supervisord"]

COPY ./supervisord.conf /etc/supervisor/supervisord.conf
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
