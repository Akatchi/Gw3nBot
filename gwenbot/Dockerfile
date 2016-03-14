FROM python:onbuild

RUN echo "Europe/Amsterdam" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

RUN easy_install pip

ADD requirements.txt /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt