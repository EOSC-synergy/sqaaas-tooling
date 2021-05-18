FROM python:3-slim

LABEL maintainer="davrodgon@users.noreply.github.com"

RUN pip3 install PyGithub python-gitlab

COPY checkCitable.py /  

ENTRYPOINT [ "python","/checkCitable.py" ]
