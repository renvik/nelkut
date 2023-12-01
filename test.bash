if [ -f .env.test ]; then
	export $(grep -v '^#' .env.test | xargs)
fi

psql "$DATABASE" < test_schema.sql

poetry run coverage run --branch -m pytest -s
poetry run coverage html
