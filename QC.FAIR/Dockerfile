FROM python:3

LABEL authors="Fernando Aguilar <aguilarf@ifca.unican.es>, Pablo Orviz <orviz@ifca.unican.es>"

# FAIR-eva client
COPY fair-eva.py /usr/bin/fair-eva.py
RUN chmod +x /usr/bin/fair-eva.py

# Deploy FAIR-eva API
WORKDIR /FAIR_eva
RUN git clone https://github.com/EOSC-synergy/FAIR_eva.git .
RUN pip3 install -r requirements.txt

RUN cp config.ini.template config.ini
EXPOSE 9090
ENTRYPOINT ["/FAIR_eva/fair.py"]
