FROM yakworks/bullseye:docker-jdk11

RUN apt-get update
RUN apt-get install python3 python3-pip openssh-client -y 

# RUN apt-get install python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 -y

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

# Application environment
WORKDIR /app
RUN pip3 install django

COPY ./erp/ /app/
 
# RUN pip3 install -r /app/requerimientos.txt

# COPY ./hosts /etc/

# RUN service apache2 restart

EXPOSE 80

CMD ["python3", "/app/manage.py", "runserver", "0.0.0.0:80"]
# CMD ["apachectl", "-D", "FOREGROUND"]