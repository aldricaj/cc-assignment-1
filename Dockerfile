FROM python:3.7.3

EXPOSE 5080
WORKDIR /usr/src/app

# Install mongo
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.2 main" | tee /etc/apt/sources.list.d/mongodb-org-4.2.list
RUN apt-get update
RUN apt-get install -y mongodb-org

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD [ "python", "./main.py" ]