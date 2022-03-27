# coding: utf-8

from typing import Any, Dict, List, Optional, Union  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)
from openapi_server import processor
from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.order import Order
from openapi_server.security_api import get_token_api_key

router = APIRouter()
response_type = Optional[Dict[Union[int, str], Dict[str, Any]]]


# delete_order ########################################################################
responses_delete_order: response_type = {
    400: {"description": "Invalid ID supplied"},
    404: {"description": "Order not found"},
}


@router.delete(
    "/store/order/{orderId}",
    responses=responses_delete_order,
    tags=["store"],
    summary="Delete purchase order by ID",
)
async def delete_order(
    orderId: str = Path(None, description="ID of the order that needs to be deleted"),
) -> None:
    """For valid response try integer IDs with value &lt; 1000. Anything above 1000 or nonintegers will generate API errors"""
    return processor.store.delete_order(
        orderId,
    )


# get_inventory ########################################################################
responses_get_inventory: response_type = {
    200: {"model": Dict[str, int], "description": "successful operation"},
}


@router.get(
    "/store/inventory",
    responses=responses_get_inventory,
    tags=["store"],
    summary="Returns pet inventories by status",
)
async def get_inventory(
    token_api_key: TokenModel = Security(get_token_api_key),
) -> Dict[str, int]:
    """Returns a map of status codes to quantities"""
    return processor.store.get_inventory(
        token_api_key,
    )


# get_order_by_id ########################################################################
responses_get_order_by_id: response_type = {
    200: {"model": Order, "description": "successful operation"},
    400: {"description": "Invalid ID supplied"},
    404: {"description": "Order not found"},
}


@router.get(
    "/store/order/{orderId}",
    responses=responses_get_order_by_id,
    tags=["store"],
    summary="Find purchase order by ID",
)
async def get_order_by_id(
    orderId: int = Path(None, description="ID of pet that needs to be fetched", ge=1, le=5),
) -> Order:
    """For valid response try integer IDs with value &lt;&#x3D; 5 or &gt; 10. Other values will generated exceptions"""
    return processor.store.get_order_by_id(
        orderId,
    )


# place_order ########################################################################
responses_place_order: response_type = {
    200: {"model": Order, "description": "successful operation"},
    400: {"description": "Invalid Order"},
}


@router.post(
    "/store/order",
    responses=responses_place_order,
    tags=["store"],
    summary="Place an order for a pet",
)
async def place_order(
    order: Order = Body(None, description="order placed for purchasing the pet"),
) -> Order:

    return processor.store.place_order(
        order,
    )
