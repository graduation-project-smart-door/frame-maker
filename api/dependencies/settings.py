from starlette.requests import Request

from core.settings import AppSettings


def get_settings(request: Request) -> AppSettings:
    return request.app.state.config
