# coding: utf-8

from typing import Any, Dict, List, Optional, Union # noqa: F401

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
from openapi_server.models.user import User
from openapi_server.security_api import get_token_api_key

router = APIRouter()
responce_type = Optional[Dict[Union[int, str], Dict[str, Any]]]


# create_user ########################################################################
responses_create_user: responce_type = {
    200: {"description": "successful operation"},
}
@router.post(
    "/user",
    responses=responses_create_user,
    tags=["user"],
    summary="Create user",
)
async def create_user(
    user: User = Body(None, description="Created user object"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    """This can only be done by the logged in user."""return processor.user.create_user(
        user,
        token_api_key,
    )



# create_users_with_array_input ########################################################################
responses_create_users_with_array_input: responce_type = {
    200: {"description": "successful operation"},
}
@router.post(
    "/user/createWithArray",
    responses=responses_create_users_with_array_input,
    tags=["user"],
    summary="Creates list of users with given input array",
)
async def create_users_with_array_input(
    user: List[User] = Body(None, description="List of user object"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    return processor.user.create_users_with_array_input(
        user,
        token_api_key,
    )



# create_users_with_list_input ########################################################################
responses_create_users_with_list_input: responce_type = {
    200: {"description": "successful operation"},
}
@router.post(
    "/user/createWithList",
    responses=responses_create_users_with_list_input,
    tags=["user"],
    summary="Creates list of users with given input array",
)
async def create_users_with_list_input(
    user: List[User] = Body(None, description="List of user object"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    return processor.user.create_users_with_list_input(
        user,
        token_api_key,
    )



# delete_user ########################################################################
responses_delete_user: responce_type = {
    400: {"description": "Invalid username supplied"},
    404: {"description": "User not found"},
}
@router.delete(
    "/user/{username}",
    responses=responses_delete_user,
    tags=["user"],
    summary="Delete user",
)
async def delete_user(
    username: str = Path(None, description="The name that needs to be deleted"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    """This can only be done by the logged in user."""return processor.user.delete_user(
        username,
        token_api_key,
    )



# get_user_by_name ########################################################################
responses_get_user_by_name: responce_type = {
    200: {"model": User, "description": "successful operation"},
    400: {"description": "Invalid username supplied"},
    404: {"description": "User not found"},
}
@router.get(
    "/user/{username}",
    responses=responses_get_user_by_name,
    tags=["user"],
    summary="Get user by user name",
)
async def get_user_by_name(
    username: str = Path(None, description="The name that needs to be fetched. Use user1 for testing."),
) -> User:
    return processor.user.get_user_by_name(
        username,
    )



# login_user ########################################################################
responses_login_user: responce_type = {
    200: {"model": str, "description": "successful operation"},
    400: {"description": "Invalid username/password supplied"},
}
@router.get(
    "/user/login",
    responses=responses_login_user,
    tags=["user"],
    summary="Logs user into the system",
)
async def login_user(
    username: str = Query(None, description="The user name for login", regex=r"^[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*[a-zA-Z0-9]+$"),
    password: str = Query(None, description="The password for login in clear text"),
) -> str:
    return processor.user.login_user(
        username,
        password,
    )



# logout_user ########################################################################
responses_logout_user: responce_type = {
    200: {"description": "successful operation"},
}
@router.get(
    "/user/logout",
    responses=responses_logout_user,
    tags=["user"],
    summary="Logs out current logged in user session",
)
async def logout_user(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    return processor.user.logout_user(
        token_api_key,
    )



# update_user ########################################################################
responses_update_user: responce_type = {
    400: {"description": "Invalid user supplied"},
    404: {"description": "User not found"},
}
@router.put(
    "/user/{username}",
    responses=responses_update_user,
    tags=["user"],
    summary="Updated user",
)
async def update_user(
    username: str = Path(None, description="name that need to be deleted"),
    user: User = Body(None, description="Updated user object"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    """This can only be done by the logged in user."""return processor.user.update_user(
        username,
        user,
        token_api_key,
    )
