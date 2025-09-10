FROM ubuntu:latest

COPY requirements.txt ./


RUN apt-get -y update
#RUN apt-get install source
RUN apt-get -y install git
RUN apt-get -y install python3
RUN apt-get -y install pip
RUN apt-get -y install python3.12-venv

RUN git clone https://github.com/OphidiaBigData/PyOphidia -b release
#RUN cd PyOphidia
WORKDIR PyOphidia
#RUN python3 -m venv . ; . bin/activate ; python3 -m pip install ".[convert,cwl,prov,display]"
RUN ls bin/

RUN python3 -m pip install ".[convert,cwl,prov,display]"
COPY find_oph_workflows.py PyOphidia/

RUN chmod +x PyOphidia/find_oph_workflows.py
RUN pwd
RUN ls
  
RUN cd ..

