FROM python:3-slim

RUN pip install os json argparse urllib requests
RUN pip install json
RUN pip install argparse
RUN pip install urllib
RUN pip install requests
RUN pip install pyophidia
COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py
