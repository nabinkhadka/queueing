FROM python:3.11-slim-bullseye
RUN apt-get update && apt-get install git -y
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
WORKDIR /app
COPY app .

