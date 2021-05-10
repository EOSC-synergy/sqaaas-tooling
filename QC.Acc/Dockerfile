FROM python:3

LABEL maintainer="davrodgon@users.noreply.github.com"

RUN pip3 install PyGithub python-gitlab

COPY checkCitable.py /usr/local/bin/
RUN chmod +x /usr/local/bin/checkCitable.py  

ENTRYPOINT [ "/usr/local/bin/checkCitable.py" ]
