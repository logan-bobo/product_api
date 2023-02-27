run:
	flask --app app run

create-supplier:
	curl -X POST 127.0.0.1:5000/v1/suppliers -H 'Content-Type: application/json' -d '{"name":"barry"}'