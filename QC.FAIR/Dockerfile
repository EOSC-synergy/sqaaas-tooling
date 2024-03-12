FROM python:3

LABEL authors="Pablo Orviz <orviz@ifca.unican.es>, Fernando Aguilar <aguilarf@ifca.unican.es>"

# Deploy FAIR-eva API
WORKDIR /FAIR_eva
RUN git clone https://github.com/EOSC-synergy/FAIR_eva.git -b 2.0.0 .
RUN pip3 install -r requirements.txt

# FAIR-eva client
RUN cp /FAIR_eva/scripts/fair-eva.py /usr/bin/fair-eva.py
RUN chmod +x /usr/bin/fair-eva.py

# Set config & run
RUN cp config.ini.template config.ini
EXPOSE 9090
ENTRYPOINT ["/FAIR_eva/fair.py"]
