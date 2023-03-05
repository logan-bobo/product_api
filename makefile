run:
	flask --app src/product_api/app run

create-supplier:
	curl -X POST 127.0.0.1:5000/v1/suppliers -H 'Content-Type: application/json' -d '{"name":"barry"}'

test:
	python -m pytest

test-unit:
	python -m pytest src/tests/unit/

test-integration:
	python -m pytest src/tests/integration/

lint:
	black src --diff --check
	isort src --profile black --check --diff
	black src --diff --check
	mypy src
	pylint src

fmt:
	black src
	isort src --profile black
