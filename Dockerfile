FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y gcc python3-dev libxslt1-dev libssl-dev libffi-dev libkrb5-dev graphviz  graphviz-dev gunicorn

RUN pip install --upgrade pip

WORKDIR /code
COPY online_store_on_sofa_project /code/

RUN pip install -r requirements.txt



