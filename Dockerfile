FROM centos:7

ENV LC_ALL en_US.utf8

RUN yum install epel-release -y
RUN yum install python36 which -y
#RUN yum install npm -y

RUN pip3 install pipenv

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.36.0/install.sh | bash && \
    source ~/.bashrc && \
    nvm install stable && \
    nvm use stable

RUN mkdir /root/bmn-visualisation
COPY ./Pipfile /root/bmn-visualisation
COPY ./Pipfile.lock /root/bmn-visualisation
COPY ./server /root/bmn-visualisation/server

COPY ./nica_dash_components /root/bmn-visualisation/nica_dash_components

RUN cd /root/bmn-visualisation/nica_dash_components && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt

RUN cd /root/bmn-visualisation/nica_dash_components && \
    . venv/bin/activate && \
    source ~/.bashrc && \
    npm install && \
    npm run build

RUN cd /root/bmn-visualisation && \
    pipenv install

WORKDIR /root/bmn-visualisation

CMD /usr/local/bin/pipenv run python -m server.main