FROM nginx:1.17.8

ADD main.py /opt/app/main.py
ADD screenshot_maker.py /opt/app/screenshot_maker.py
ADD pyproject.toml /opt/app/pyproject.toml
ADD poetry.lock /opt/app/pyproject.toml

WORKDIR /opt/app

RUN apt update
    && apt install python3.7
    && pip install poetry
    && cd /opt/app
    && poetry install

EXPOSE 8080
