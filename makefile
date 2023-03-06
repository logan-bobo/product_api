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
	black . --diff --check
	isort . --profile black --check --diff
	mypy .
	pylint .

fmt:
	black .
	isort . --profile black
