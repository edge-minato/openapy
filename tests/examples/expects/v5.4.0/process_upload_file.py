
# coding: utf-8

from typing import Dict, List # noqa: F401
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status # noqa: F401
from openapi_server.models.extra_models import TokenModel # noqa: F401
from openapi_server.models.api_response import ApiResponse # noqa: F401
from openapi_server.models.pet import Pet # noqa: F401
from openapi_server.security_api import get_token_petstore_auth, get_token_api_key # noqa: F401

async def process_upload_file(petId: int, additional_metadata: str, file: str, token_petstore_auth: TokenModel) -> ApiResponse:
    """Ellipsis"""
    # implement me
    ...
