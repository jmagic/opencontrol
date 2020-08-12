FROM python:3.7-buster

#install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


#copy source and install dependancies
RUN mkdir -p /opt/jims_av
RUN mkdir -p /opt/jims_av/pip_cache
#RUN mkdir -p /opt/jims_av/plankowner
RUN mkdir -p /opt/jims_av/zenav
COPY requirements.txt start-server.sh /opt/jims_av/
#COPY .pip_cache /opt/jims_av/pip_cache/
#COPY plankowner /opt/jims_av/plankowner/
COPY zenav /opt/jims_av/zenav/
WORKDIR /opt/jims_av
RUN pip install -r requirements.txt --cache-dir /opt/jims_av/pip_cache
RUN chown -R www-data:www-data /opt/jims_av

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/jims_av/start-server.sh"]
