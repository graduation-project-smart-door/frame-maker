import sqlalchemy
from fastapi import FastAPI

from databases import Database
from loguru import logger

from core.settings import AppSettings
from database.models import BaseModel


async def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    logger.info('Connecting to sqlite')

    db = Database(settings.database_url)
    await db.connect()

    metadata = BaseModel.metadata
    dialect = sqlalchemy.dialects.sqlite.dialect()
    for table in metadata.tables.values():
        schema = sqlalchemy.schema.CreateTable(table, if_not_exists=True)
        query = str(schema.compile(dialect=dialect))
        await db.execute(query=query)

    app.state.pool = db

    logger.info('Connection established')


async def close_db_connection(app: FastAPI) -> None:
    logger.info('Closing connection to database')

    await app.state.pool.disconnect()

    logger.info('Connection closed')
