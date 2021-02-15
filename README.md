# Metrico-Backend-on-Docker
In order to run the docker run the following commands: (please make sure the Docker is updated and running. For development env use docker-compose.yml).
1. docker-compose -f docker-compose.prod.yml down -v
2. docker-compose -f docker-compose.prod.yml up -d --build
3. docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
