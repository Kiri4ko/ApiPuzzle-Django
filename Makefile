run:
	python manage.py runserver $(port)
migrate:
	python manage.py makemigrations $(name)
	python manage.py migrate
startapp:
	python manage.py startapp $(name)
superuser:
	python manage.py createsuperuser
shell:
	python manage.py shell
generate-dependencies:
	poetry export --without-hashes -f requirements.txt --output requirements-dev.txt --dev
	poetry export --without-hashes -f requirements.txt --output requirements.txt
pre-commit:
	poetry run python manage.py test
	poetry run flake8 .