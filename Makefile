b: docker-compose.yml
	docker-compose build

bn: docker-compose.yml
	docker-compose build --no-cache

s: docker-compose.yml
	docker-compose up -d postgres
	sleep 3
	docker-compose up -d web

mm:
	docker-compose exec web python manage.py makemigrations

m:
	docker-compose exec web python manage.py migrate

cs:
	docker-compose exec web python manage.py collectstatic --noinput -l

csu:
	docker-compose exec web python manage.py createsuperuser

sh:
	docker-compose exec web python manage.py shell

i: s m cs

l:
	docker-compose logs -f

r:
	docker-compose restart

stop:
	docker-compose stop

d:
	docker-compose down --volumes
