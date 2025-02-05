FROM python:3-slim

RUN pip install os json argparse urllib requests

COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py
