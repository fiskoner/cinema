FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /cinema
WORKDIR /cinema
ADD requirements.txt /cinema/
RUN pip3 install --no-cache-dir -r requirements.txt
ADD . /cinema/