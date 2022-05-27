FROM ubuntu:20.04

MAINTAINER Fernando Aguilar "aguilarf@ifca.unican.es"

RUN apt-get update -y && \
    apt-get install -y curl python3-pip python3-dev git vim lsof

RUN git clone https://github.com/EOSC-synergy/FAIR_eva.git

WORKDIR /FAIR_eva

RUN pip3 install -r requirements.txt

EXPOSE 5000 9090
RUN cp config.ini.template config.ini
RUN cd /FAIR_eva
RUN chmod 777 start.sh
RUN cat start.sh
COPY fair-eva.py /usr/bin
RUN chmod +x /usr/bin/fair-eva.py
ENV CONFIG_FILE=/FAIR_eva/config.ini
CMD ["/FAIR_eva/start.sh", "/FAIR_eva/config.ini"]
