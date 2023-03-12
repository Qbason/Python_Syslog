FROM ubuntu:22.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
#disable input during install packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
#install apache and  needed packages
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
#install useful packages for apache 
RUN apt-get install -y alpine
#make dir to our code
RUN mkdir /code/
# make our dir default for commands like RUN, CMD etc.
WORKDIR /code/
#copy code and configuration
COPY ./frontend/build /code/build
#copy our certs for https!
#COPY http.conf
ADD ./frontend/http.conf /etc/apache2/sites-available/http.conf
ADD ./frontend/ports.conf /etc/apache2/ports.conf
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
CMD ["apache2ctl", "-D", "FOREGROUND"]
