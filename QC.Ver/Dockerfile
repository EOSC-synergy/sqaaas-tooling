FROM python:3.9-alpine
LABEL maintainer="Pablo Orviz <orviz@ifca.unican.es>"
RUN apk --no-cache add build-base
RUN python3 -m pip install GitPython==3.1.27
COPY get_git_tags.py /usr/bin
RUN chmod +x /usr/bin/get_git_tags.py
