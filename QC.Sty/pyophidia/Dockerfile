FROM python:3.12

COPY requirements.txt ./
COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py

RUN apt-get -y update
RUN apt-get source
#RUN apt-get -y install git
#RUN apt-get -y install python3
#RUN apt-get -y install pip

RUN git clone https://github.com/OphidiaBigData/PyOphidia -b release
RUN cd PyOphidia

RUN python3 -m venv opt
RUN ls opt/bin/
RUN source opt/bin/

RUN python3 -m pip install ".[convert,cwl,prov,display]"
RUN cd ..

