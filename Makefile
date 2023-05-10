setup-dev:
	pip install poetry
	poetry install --with dev

setup-prod:
	pip install poetry
	poetry install

lint:
	poetry run pre-commit run -a

run:
	poetry run python main.py