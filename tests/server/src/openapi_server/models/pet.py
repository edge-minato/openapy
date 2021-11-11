# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from openapi_server.models.category import Category
from openapi_server.models.tag import Tag
from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Pet(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Pet - a model defined in OpenAPI

        id: The id of this Pet [Optional].
        category: The category of this Pet [Optional].
        name: The name of this Pet.
        photo_urls: The photo_urls of this Pet.
        tags: The tags of this Pet [Optional].
        status: The status of this Pet [Optional].
    """

    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photo_urls: List[str]
    tags: Optional[List[Tag]] = None
    status: Optional[str] = None

Pet.update_forward_refs()
