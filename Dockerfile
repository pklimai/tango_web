FROM centos:7

ENV LC_ALL en_US.utf8

RUN yum install epel-release -y
RUN yum install python36 which -y

RUN pip3 install pipenv

RUN mkdir /root/bmn-visualisation
COPY ./Pipfile /root/bmn-visualisation
COPY ./Pipfile.lock /root/bmn-visualisation
COPY ./server /root/bmn-visualisation/server

RUN cd /root/bmn-visualisation && \
    pipenv install

WORKDIR /root/bmn-visualisation

CMD /usr/local/bin/pipenv run python -m server.main