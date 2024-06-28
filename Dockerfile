FROM python:3.11-slim-bullseye
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
WORKDIR /app
COPY app .

