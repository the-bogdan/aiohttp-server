FROM python:3.9-slim as base

FROM base as builder
LABEL stage=builder
RUN apt-get update && apt-get install gcc -y
RUN mkdir -p /install
COPY ./requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY ./app /opt/flask_app
WORKDIR /opt/flask_app
ENV PYTHONPATH $PYTHONPATH:/opt/flask_app

ENTRYPOINT ["bash", "./entrypoint.sh"]
