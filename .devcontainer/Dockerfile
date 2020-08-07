FROM matthijsbos/nerdrage-dev:latest

COPY ../requirements.txt /tmp/
COPY ../requirements_test.txt /tmp/
COPY ../requirements_dev.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements_test.txt
RUN pip3 install -r /tmp/requirements_dev.txt
RUN curl -L https://raw.githubusercontent.com/docker/compose/1.26.2/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose

