if [ -f .env.test ]; then
	export $(grep -v '^#' .env.test | xargs)
fi

psql "$DATABASE" < schema.sql
