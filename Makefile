run-aws:
	docker-compose -f docker-compose.aws.yml up --build -d

collectstatic:
	docker-compose -f docker-compose.aws.yml exec web python manage.py collectstatic --no-input --clear

migrate:
	docker-compose -f docker-compose.aws.yml exec web python manage.py migrate --no-input

