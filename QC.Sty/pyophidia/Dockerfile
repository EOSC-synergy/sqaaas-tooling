FROM ubuntu/python:3.12-24.04_stable


COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py
