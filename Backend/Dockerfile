FROM yakworks/bullseye:docker-jdk11

RUN apt-get update
RUN apt install pkg-config libmariadb-dev -y
RUN apt-get install default-libmysqlclient-dev build-essential python3 python3-pip openssh-client python3-dev -y 

# RUN apt-get install python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 -y

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

# Application environment
WORKDIR /app

COPY ./erp/ /app/

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r /app/requirements.txt

# COPY ./hosts /etc/

# RUN service apache2 restart

EXPOSE 80

CMD ["python3", "/app/manage.py", "runserver", "0.0.0.0:80"]
# CMD ["apachectl", "-D", "FOREGROUND"]