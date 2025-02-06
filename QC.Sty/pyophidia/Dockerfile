FROM python:3

#RUN pip install os
#RUN pip install json
#RUN pip install argparse
#RUN pip install urllib
#RUN pip install requests
#RUN pip install pyophidia

COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py
