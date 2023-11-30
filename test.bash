DB_URL=postgresql:///nelkut_tests

psql "$DB_URL" < test_schema.sql

poetry run pytest
