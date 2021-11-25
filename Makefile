populate:
	docker exec lab04_python python /apps/populate.py

query:
	docker exec -t lab04_python bash -c "time IS_PREPARED=${IS_PREPARED} python /apps/query.py"
