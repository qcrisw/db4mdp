FROM python:3.6
LABEL maintainer="Alaa Hamoudah <ahammouda@qcri.org>"
WORKDIR /home

#install postgress and all it's dependencies in this container
RUN apt-get update -qq && \
    apt-get install -y \
        libpq-dev python3-dev \
        #postgresql-9.6 i don't need this anymore because i'm going to be connecting to the online postgres server
        #and i don't have to host the server on the local machine anymore.
        postgresql-client-9.6

# copy requirements first to cache the deps
COPY requirements.txt /home

RUN pip install -r requirements.txt
#doesnt work when done from requirements files for some reason
#RUN pip install geoip2
#RUN pip install git+https://github.com/bashu/django-tracking.git

COPY / /home

CMD ["./shell.sh"]

EXPOSE 8000