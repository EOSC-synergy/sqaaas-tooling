FROM python:3.10

COPY requirements.txt ./
COPY find_oph_workflows.py /usr/bin

RUN chmod +x /usr/bin/find_oph_workflows.py


RUN git clone https://github.com/OphidiaBigDataPyiphidia.git
RUN cd PyOphidia
RUN git checkout release
RUN python -m pip install ".[convert,cwl,prov,display]"#pip install -r requirements.txt
RUN cd ..

