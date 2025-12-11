#!/usr/bin/env bash
set -e

# first arg is the DB host (we pass "db" from docker-compose)
DB_HOST=${1:-db}

# Wait for Postgres to be ready
echo "Waiting for Postgres at $DB_HOST..."
until pg_isready -h "$DB_HOST" -p 5432 -U "$POSTGRES_USER" >/dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Postgres is up - continuing"

# Run Alembic migrations (safe no-op if none)
echo "Running alembic upgrade head"
alembic upgrade head

# Start the FastAPI server
echo "Starting uvicorn"
exec uvicorn main:app --host 0.0.0.0 --port 8000
