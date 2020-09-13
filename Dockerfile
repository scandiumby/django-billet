FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements_dev.txt /code/
RUN pip install -r requirements_dev.txt
COPY . /code/