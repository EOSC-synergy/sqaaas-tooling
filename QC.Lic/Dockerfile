FROM python:3-slim
LABEL maintainer="davrodgon@users.noreply.github.com"
RUN pip3 install PyGithub python-gitlab
COPY QC.Lic/checkLicense.py /
ENTRYPOINT [ "python","/checkLicense.py" ]

FROM ruby:2.5
RUN apt-get update && apt-get install -y \
  cmake \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
RUN gem install licensee
COPY --from=0 /checkLicense.py .
