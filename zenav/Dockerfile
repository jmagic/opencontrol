FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /opencontrol
WORKDIR /opencontrol
COPY requirements.txt /opencontrol
RUN pip install -r requirements.txt
COPY . /opencontrol