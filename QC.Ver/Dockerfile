FROM bitnami/git:2.34.1
LABEL maintainer="Pablo Orviz <orviz@ifca.unican.es>"
RUN apt-get update && apt-get install -y \
  python3 python3-pip \
  && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install GitPython==3.1.27
COPY get_git_tags.py /usr/bin
RUN chmod +x /usr/bin/get_git_tags.py
