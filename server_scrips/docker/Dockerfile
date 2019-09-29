FROM google/dart

FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb

# install chromedriver and google-chrome

RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

RUN CHROME_SETUP=google-chrome.deb && \
    wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP && \
    apt-get install -y -f && \
    rm $CHROME_SETUP

RUN pip3 install selenium

WORKDIR /app
ADD pubspec.* /app/

RUN groupadd -r aqueduct
RUN useradd -m -r -g aqueduct aqueduct
RUN chown -R aqueduct:aqueduct /app

USER aqueduct
RUN pub get --no-precompile

USER root
ADD . /app
RUN chown -R aqueduct:aqueduct /app

USER aqueduct
RUN pub get --offline --no-precompile

EXPOSE 8082

ENTRYPOINT ["pub", "run", "aqueduct:aqueduct", "serve", "--port", "8082"]
