# pull official base image
FROM python:3.7.3-alpine

# set work directory
#WORKDIR /Users/israelsach/Metrico-Backend-on-Docker/django-app/metrico_api
WORKDIR /my-work-dir
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
#ENTRYPOINT ["/Users/israelsach/Metrico-Backend-on-Docker/django-app/metrico_api/entrypoint.sh"]
ENTRYPOINT ["/my-work-dir/entrypoint.sh"]