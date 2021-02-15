# Metrico-Backend-on-Docker
In order to run the docker in production env run the following commands: (please make sure the Docker is updated and running.)
1. docker-compose -f docker-compose.prod.yml down -v
2. docker-compose -f docker-compose.prod.yml up -d --build
3. docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
4. docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
5. go to http://localhost:1337/

In order to run the docker in development env run the following commands: (please make sure the Docker is updated and running.)
1. docker-compose -f docker-compose.yml down -v
2. docker-compose -f docker-compose.yml up -d --build
3. docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
4. go to http://localhost:8000/
