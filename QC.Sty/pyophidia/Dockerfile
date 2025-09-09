FROM ubuntu:latest

COPY requirements.txt ./
COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py

RUN apt-get -y update
#RUN apt-get install source
RUN apt-get -y install git
RUN apt-get -y install python3
RUN apt-get -y install pip
RUN apt-get -y install python3.12-venv

RUN git clone https://github.com/OphidiaBigData/PyOphidia -b release
RUN cd PyOphidia

RUN python3 -m venv opt
RUN ls opt/bin/
#RUN source opt/bin/

RUN pwd
RUN ls

RUN python3 -m pip install ".[convert,cwl,prov,display]" --break-system-packages
RUN cd ..

