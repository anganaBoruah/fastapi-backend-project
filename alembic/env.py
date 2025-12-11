import asyncio
import os
import sys
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

# --- Alembic Config ---
config = context.config

# Logging config
fileConfig(config.config_file_name)

# Make sure project root is in PYTHONPATH
sys.path.append(".")

# Import metadata from your models
from app.db import Base  # IMPORTANT: adjust only if db.py is elsewhere

target_metadata = Base.metadata


# --- Offline migrations (generate SQL only) ---
def run_migrations_offline():
    url = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@db:5432/myapp"
    )

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# --- Online migrations (real DB migrations) ---
def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    url = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@db:5432/myapp"
    )

    # Create async engine
    connectable = create_async_engine(
        url,
        poolclass=pool.NullPool,
        future=True,
    )

    # Connect and run migrations in sync mode
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


# --- Entrypoint ---
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
