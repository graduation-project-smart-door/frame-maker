from typing import List

from pydantic import BaseSettings, PostgresDsn


class AppSettings(BaseSettings):
    debug: bool = False
    database_url: PostgresDsn

    allowed_hosts: List[str] = ['*']

    class Config:
        validate_assignment = True
        env_file = '.env'


def get_app_settings() -> AppSettings:
    return AppSettings()