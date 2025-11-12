
FROM ubuntu:22.04

RUN  apt-get update &&  apt-get install -y  pip git

COPY requirements.txt ./
COPY ls.txt ./
RUN pip install -r requirements.txt #--break-system-packages 
COPY notebook_evaluator.py /usr/bin
RUN  chmod +x /usr/bin/notebook_evaluator.py



#RUN  git clone https://gitlab.a.incd.pt/envri-hub-next/analytical-workflow-templates
