# Dockerfile with SCRIPT TITLE
# author: YOUR NAME
# version: 1.0.0

FROM python:3.12.0

LABEL maintainer="you@yourname.com"

RUN mkdir app
COPY requirements.txt app
COPY main.py app
COPY gui/streamlit_app.py app
WORKDIR app
RUN pip install -r requirements.txt
RUN pip install streamlit

CMD  ["streamlit", "run", "streamlit_app.py"]
