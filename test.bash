DB_URL=postgresql://postgres:savusauna@localhost:5432/nelkut_tests

psql "$DB_URL" < "$(dirname $0)\test_schema.sql"

poetry run pytest
