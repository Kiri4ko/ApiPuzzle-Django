run:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
superuser:
	python manage.py createsuperuser
generate-dependencies:
	poetry export --without-hashes -f requirements.txt --output requirements-dev.txt --dev
	poetry export --without-hashes -f requirements.txt --output requirements.txt
pre-commit:
	poetry run python manage.py test
	poetry run flake8 .