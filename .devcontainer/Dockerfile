FROM python:3.12-slim

ARG USERNAME=user
ARG NVM_VERSION=0.39.7
ARG NODE_VERSION=20.14.0
ARG NVM_DIR=/usr/local/nvm

USER root

RUN apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y --no-install-recommends \
  locales \
  tzdata \
  git \
  ca-certificates \
  openssh-client \
  curl \
  && apt-get -y autoclean \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN locale-gen ja_JP.UTF-8 \
  && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV TZ=Asia/Tokyo \
  LANG=ja_JP.UTF-8 \
  LANGUAGE=ja_JP:jp \
  LC_ALL=ja_JP.UTF-8

RUN pip install --upgrade pip setuptools

RUN mkdir -p $NVM_DIR \
  && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v$NVM_VERSION/install.sh | bash \
  && . $NVM_DIR/nvm.sh \
  && nvm install $NODE_VERSION \
  && nvm alias default $NODE_VERSION \
  && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN groupadd -r $USERNAME && useradd -r -g $USERNAME $USERNAME
RUN mkdir -p /home/$USERNAME/workspace

WORKDIR /home/$USERNAME/workspace

COPY --chown=$USERNAME:$USERNAME ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

USER $USERNAME

ENTRYPOINT [ "/bin/bash" ]
