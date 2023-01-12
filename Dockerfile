FROM python:3.11.1-alpine3.17

LABEL Maintainer="serega404"

WORKDIR /app

COPY main.py main.py
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container
CMD ["/usr/sbin/crond", "-f"]