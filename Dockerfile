FROM python:3.7-alpine
WORKDIR /fib
COPY requirements.txt .
RUN pip install -r requirements.txt
