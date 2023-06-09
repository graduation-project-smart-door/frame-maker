from typing import Callable

from fastapi import FastAPI
from loguru import logger

from core.settings import AppSettings
from database.events import close_db_connection, connect_to_db


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app, settings)

    app.state.config = settings
    return start_app


def create_stop_app_handler(app: FastAPI):
    @logger.catch
    async def stop_app() -> None:
        await close_db_connection(app)
