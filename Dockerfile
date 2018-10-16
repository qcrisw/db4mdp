FROM python:3.6
LABEL maintainer="Alaa Hamoudah <ahammouda@qcri.org>"
WORKDIR /home

#install postgress and all it's dependencies in this container
RUN apt-get update -qq && \
    apt-get install -y \
        libpq-dev python3-dev \
        postgresql-9.6 \
        postgresql-client-9.6

# copy requirements first to cache the deps
COPY requirements.txt /home

RUN pip install -r requirements.txt
COPY / /home

CMD ["./shell.sh"]

EXPOSE 8000