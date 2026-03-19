
FROM python:3.10

RUN  apt-get update &&  apt-get install -y  pip git

COPY requirements.txt ./
COPY ls.txt ./
RUN pip install -r requirements.txt #--break-system-packages
COPY pynblint.py /usr/bin
RUN  chmod +x /usr/bin/pynblint.py



#RUN  git clone https://gitlab.a.incd.pt/envri-hub-next/analytical-workflow-templates
