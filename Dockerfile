FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    libgdal-dev \
    gdal-bin \
    python3-gdal \
    postgresql-client
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
