FROM python:3.8-slim-buster

ENV FLASK_APP exceptions_api.py
ENV DATADOG_ENV flask_test

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "ddtrace-run", "python3", "exceptions_api.py"]
