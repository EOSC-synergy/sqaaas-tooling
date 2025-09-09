FROM ubuntu

COPY requirements.txt ./
COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py

RUN apt-get -y update
RUN apt-get -y install git

RUN git clone https://github.com/OphidiaBigData/PyOphidia -b release
RUN cd PyOphidia

RUN sudo python -m pip install ".[convert,cwl,prov,display]"
RUN cd ..

