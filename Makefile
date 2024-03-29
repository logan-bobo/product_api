run:
	flask --app src/product_api/app run --debug

create-supplier:
	curl -X POST 127.0.0.1:5000/v1/suppliers -H 'Content-Type: application/json' -d '{"name":"aasasddsadasdasasdasdsdaasddasasddasdasdasdasaasdasdadsdsasdaadsasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"}'
	curl -X POST 127.0.0.1:5000/v1/suppliers -H 'Content-Type: application/json' -d '{"name":"larry"}'
	curl -X POST 127.0.0.1:5000/v1/suppliers -H 'Content-Type: application/json' -d '{"name":"garry"}'

test:
	python -m pytest -s

test-unit:
	python -m pytest src/tests/unit/

test-integration:
	python -m pytest src/tests/integration/

lint:
	black src/ --diff --check
	isort src/ --profile black --check --diff
	mypy src/
	pylint src/

fmt:
	black .
	isort . --profile black
