
# coding: utf-8

from typing import Dict, List # noqa: F401
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status # noqa: F401
from openapi_server.models.extra_models import TokenModel # noqa: F401
from openapi_server.models.order import Order # noqa: F401
from openapi_server.security_api import get_token_api_key # noqa: F401

async def process_delete_order(orderId: str) -> None:
    """For valid response try integer IDs with value &lt; 1000. Anything above 1000 or nonintegers will generate API errors"""
    """Ellipsis"""
    # implement me
    ...
