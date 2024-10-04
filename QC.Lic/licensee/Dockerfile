FROM ruby:3
RUN apt-get update && apt-get install -y \
  cmake \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
RUN gem install licensee
USER 1001
