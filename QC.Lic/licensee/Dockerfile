FROM ruby:2.6
RUN apt-get update && apt-get install -y \
  cmake \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
RUN gem install octokit -v 4.25.1
RUN gem install nokogiri -v 1.13.1
RUN gem install licensee
USER 1001
