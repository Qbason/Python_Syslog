FROM ubuntu:22.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
#disable input during install packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
#install apache and  needed packages
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
#install useful packages for apache 
RUN apt-get install -y alpine
#install python3 and needed mod for django
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
#python3 and python the same (shortcut)
RUN ln /usr/bin/python3 /usr/bin/python
#install pip for python
RUN apt-get -y install python3-pip
#upgrade pip and install necessary packages
RUN pip install --upgrade pip
#install virtual env
RUN apt install -y python3.10-venv
#make sure, that output goes to terminal!
ENV PYTHONUNBUFFERED 1
#make dir to our code
RUN mkdir /code/
# make our dir default for commands like RUN, CMD etc.
WORKDIR /code/
#install packages in venv python based on requirements.txt
COPY ./backend/weblogger/requirements.txt /code
RUN python3 -m venv myenv_linux
#copy code and configuration
COPY ./backend/weblogger /code/weblogger
RUN source /code/myenv_linux/bin/activate && pip install -r requirements.txt && pip install ptvsd
#COPY http.conf
ADD ./backend/weblogger/http.conf /etc/apache2/sites-available/http.conf
ADD ./backend/weblogger/ports.conf /etc/apache2/ports.conf
#enable site-available
RUN a2ensite http.conf
#enable needed mod
RUN a2enmod lbmethod_byrequests
#we need to disable npm_event and npm_worker to npm_prefork works
RUN a2dismod mpm_event
RUN a2dismod mpm_worker
RUN a2enmod mpm_prefork
RUN a2enmod authz_groupfile
RUN a2enmod headers
RUN a2enmod rewrite
#start service reload and stop
RUN service apache2 start && service apache2 reload && service apache2 stop
# EXPOSE 80 443
#to run if we don't need to command in docker-compose
# CMD ["apache2ctl", "-D", "FOREGROUND"]
