FROM redhat/ubi8

# Set the locale
#RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
#    locale-gen
# RUN localedef -i en_US -f UTF-8 en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# RUN yum install epel-release -y
RUN yum install python39 python39-pip which -y
# RUN yum install npm -y

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.36.0/install.sh | bash && \
    source ~/.bashrc && \
    nvm install 16 && \
    nvm use 16

RUN mkdir /root/bmn-visualisation
COPY ./server /root/bmn-visualisation/server
COPY ./nica_dash_components /root/bmn-visualisation/nica_dash_components
COPY ./requirements.txt /root/bmn-visualisation/

RUN cd /root/bmn-visualisation && \
    pip3 install -r requirements.txt && \
    pip3 install wheel

RUN cd /root/bmn-visualisation/nica_dash_components && \
    source ~/.bashrc &&\
    npm install && \
    npm run build

RUN cd /root/bmn-visualisation/nica_dash_components && \
    source ~/.bashrc &&\
    python3 setup.py sdist bdist_wheel

RUN pip3 install /root/bmn-visualisation/nica_dash_components/dist/nica_dash_components-0.0.1-py3-none-any.whl

WORKDIR /root/bmn-visualisation

CMD python3 -m server.main
