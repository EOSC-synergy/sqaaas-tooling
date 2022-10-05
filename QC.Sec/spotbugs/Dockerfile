FROM debian

ARG SPOTBUGS_VERSION=4.7.2

RUN apt-get update && \
    apt-get -y install curl

RUN curl https://repo.maven.apache.org/maven2/com/github/spotbugs/spotbugs/$SPOTBUGS_VERSION/spotbugs-$SPOTBUGS_VERSION.tgz -L -o spotbugs.tgz \
    && tar xvzf spotbugs.tgz \
    && rm spotbugs.tgz \
    && chmod +x /spotbugs-$SPOTBUGS_VERSION/bin/spotbugs \
    && update-alternatives --install /usr/bin/spotbugs spotbugs /spotbugs-$SPOTBUGS_VERSION/bin/spotbugs 1
