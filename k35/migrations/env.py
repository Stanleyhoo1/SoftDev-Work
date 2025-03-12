from __future__ import with_statement
import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from flask import current_app

config = context.config

fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# this will overwrite the ini-file sqlalchemy.url path with the path given in the app config
# this makes sure the migration uses the same URL as the app
config.set_main_option(
    'sqlalchemy.url', str(current_app.config.get('SQLALCHEMY_DATABASE_URI'))
)

target_metadata = current_app.extensions['migrate'].db.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()