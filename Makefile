.PHONY: migrations migrate rollback

migrations:
	alembic revision --autogenerate -m "$(message)"

migrate:
	alembic upgrade head

rollback:
	alembic downgrade -1

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: test
test:
	pytest -v

.PHONY: run
run:
	./scripts/start.sh
