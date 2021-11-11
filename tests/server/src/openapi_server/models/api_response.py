# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class ApiResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ApiResponse - a model defined in OpenAPI

        code: The code of this ApiResponse [Optional].
        type: The type of this ApiResponse [Optional].
        message: The message of this ApiResponse [Optional].
    """

    code: Optional[int] = None
    type: Optional[str] = None
    message: Optional[str] = None

ApiResponse.update_forward_refs()
