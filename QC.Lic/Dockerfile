FROM python:3

LABEL maintainer="davrodgon@users.noreply.github.com"

RUN pip3 install PyGithub

COPY checkLicense.py /usr/local/bin/
RUN chmod +x /usr/local/bin/checkLicense.py  

ENTRYPOINT [ "/usr/local/bin/checkLicense.py" ]
