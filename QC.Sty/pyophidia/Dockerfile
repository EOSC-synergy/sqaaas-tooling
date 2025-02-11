FROM python:3.10

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py

