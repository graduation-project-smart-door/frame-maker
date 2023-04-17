from typing import List

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    database_url: str
    token: str

    allowed_hosts: List[str] = ['*']

    class Config:
        validate_assignment = True
        env_file = '.env'


def get_app_settings() -> AppSettings:
    return AppSettings()
