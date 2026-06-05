# Dockerfile with SCRIPT TITLE
# author: YOUR NAME
# version: 1.0.0

FROM python:3.14

LABEL maintainer="you@yourname.com"

RUN mkdir app
COPY ./ app/
WORKDIR app

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir uv
RUN uv sync --no-cache

CMD  ["uv", "run", "streamlit", "run", "app.py"]
