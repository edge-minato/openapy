
# coding: utf-8

from typing import Dict, List # noqa: F401
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status # noqa: F401
from openapi_server.models.extra_models import TokenModel # noqa: F401
from openapi_server.models.user import User # noqa: F401
from openapi_server.security_api import get_token_api_key # noqa: F401

async def process_update_user(username: str, user: User, token_api_key: TokenModel) -> None:
    """This can only be done by the logged in user."""
    """Ellipsis"""
    # implement me
    ...
