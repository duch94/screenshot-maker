FROM python:3.7.6-buster

WORKDIR /opt/app

RUN pip install poetry

ADD pyproject.toml /opt/app/pyproject.toml
ADD poetry.lock /opt/app/poetry.lock

RUN poetry install && `poetry env info -p`/bin/pyppeteer-install
# Instaling dependencies for chrome. Chrome comes with pyppeteer
RUN apt-get update && apt-get install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 \
libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 \
libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 \
libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 \
libnss3 lsb-release xdg-utils wget
RUN mkdir -p /var/log/gunicorn

ADD main.py /opt/app/main.py
ADD screenshot_maker.py /opt/app/screenshot_maker.py
ADD logger.py /opt/app/logger.py

EXPOSE 8080

# some shit with groups: container doesn't start
RUN groupadd -g 1001 appgroup
RUN useradd -r -u 1001 -g appgroup appuser
USER appuser

CMD `poetry env info -p`/bin/gunicorn main:app_factory \
--bind 0.0.0.0:8080 \
--worker-class aiohttp.GunicornWebWorker \
--access-logfile /var/log/gunicorn/access.log \
--error-logfile /var/log/gunicorn/error.log \
--capture-output
