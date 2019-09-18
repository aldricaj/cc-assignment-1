FROM python:3.7

EXPOSE 5080
WORKDIR /usr/src/app

# Install mongo
RUN apt-get update && apt-get install -yy mongodb-org

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD [ "python", "./main.py" ]