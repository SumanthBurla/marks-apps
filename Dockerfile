# syntax=docker/dockerfile:1

# start by pulling the python image
FROM python:3.8-alpine

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY . /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# make sqlite db and some random data in it.
RUN python /app/init_db.py

# give start point for flask app.
ENV FLASK_APP=app.py

# cmd to run flask app
CMD ["flask", "run", "--host=0.0.0.0"]


# docker pull jenkins/jenkins:latest
# docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:latest
