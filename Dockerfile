FROM debian:jessie

MAINTAINER Mael R. <mael@mql.ovh>

RUN apt-get update && \
    apt-get install --force-yes -y python2.7 \
        python-pip \
        libpython2.7-dev \
        libyaml-dev \
        libffi-dev \
        libssl-dev \
        openssh-client

RUN apt-get clean; \ 
    apt-get autoremove; \
    find /var/lib/apt/lists -type f -delete

ENV APP_DIR /opt

WORKDIR ${APP_DIR}
ADD . $APP_DIR

RUN pip install --upgrade -r requirements.txt

EXPOSE 8000

VOLUME ["${APP_DIR}/playbooks", "${APP_DIR}/roles", "/root/.ssh" ]

CMD ["/bin/bash", "env.sh"]
