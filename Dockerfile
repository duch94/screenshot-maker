FROM python:3.7.6-buster

ADD main.py /opt/app/main.py
ADD screenshot_maker.py /opt/app/screenshot_maker.py
ADD pyproject.toml /opt/app/pyproject.toml
ADD poetry.lock /opt/app/poetry.lock

WORKDIR /opt/app

RUN pip install poetry
RUN poetry install && `poetry env info -p`/bin/pyppeteer-install

EXPOSE 8080

CMD `poetry env info -p`/bin/gunicorn main:app_factory --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker
