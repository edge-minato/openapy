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
from openapi_server.models.api_response import ApiResponse
from openapi_server.models.pet import Pet
from openapi_server.security_api import get_token_petstore_auth, get_token_api_key

router = APIRouter()
response_type = Optional[Dict[Union[int, str], Dict[str, Any]]]


# add_pet ########################################################################
responses_add_pet: response_type = {
    200: {"model": Pet, "description": "successful operation"},
    405: {"description": "Invalid input"},
}
@router.post(
    "/pet",
    responses=responses_add_pet,
    tags=["pet"],
    summary="Add a new pet to the store",
)
async def add_pet(
    pet: Pet = Body(None, description="Pet object that needs to be added to the store"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> Pet:
    
    return processor.add_pet(
        pet,
        token_petstore_auth,
    )



# delete_pet ########################################################################
responses_delete_pet: response_type = {
    400: {"description": "Invalid pet value"},
}
@router.delete(
    "/pet/{petId}",
    responses=responses_delete_pet,
    tags=["pet"],
    summary="Deletes a pet",
)
async def delete_pet(
    petId: int = Path(None, description="Pet id to delete"),
    api_key: str = Header(None, description=""),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> None:
    
    return processor.delete_pet(
        petId,
        api_key,
        token_petstore_auth,
    )



# find_pets_by_status ########################################################################
responses_find_pets_by_status: response_type = {
    200: {"model": List[Pet], "description": "successful operation"},
    400: {"description": "Invalid status value"},
}
@router.get(
    "/pet/findByStatus",
    responses=responses_find_pets_by_status,
    tags=["pet"],
    summary="Finds Pets by status",
)
async def find_pets_by_status(
    status: List[str] = Query(None, description="Status values that need to be considered for filter"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["read:pets"]
    ),
) -> List[Pet]:
    """Multiple status values can be provided with comma separated strings"""
    return processor.find_pets_by_status(
        status,
        token_petstore_auth,
    )



# find_pets_by_tags ########################################################################
responses_find_pets_by_tags: response_type = {
    200: {"model": List[Pet], "description": "successful operation"},
    400: {"description": "Invalid tag value"},
}
@router.get(
    "/pet/findByTags",
    responses=responses_find_pets_by_tags,
    tags=["pet"],
    summary="Finds Pets by tags",
)
async def find_pets_by_tags(
    tags: List[str] = Query(None, description="Tags to filter by"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["read:pets"]
    ),
) -> List[Pet]:
    """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing."""
    return processor.find_pets_by_tags(
        tags,
        token_petstore_auth,
    )



# get_pet_by_id ########################################################################
responses_get_pet_by_id: response_type = {
    200: {"model": Pet, "description": "successful operation"},
    400: {"description": "Invalid ID supplied"},
    404: {"description": "Pet not found"},
}
@router.get(
    "/pet/{petId}",
    responses=responses_get_pet_by_id,
    tags=["pet"],
    summary="Find pet by ID",
)
async def get_pet_by_id(
    petId: int = Path(None, description="ID of pet to return"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> Pet:
    """Returns a single pet"""
    return processor.get_pet_by_id(
        petId,
        token_api_key,
    )



# update_pet ########################################################################
responses_update_pet: response_type = {
    200: {"model": Pet, "description": "successful operation"},
    400: {"description": "Invalid ID supplied"},
    404: {"description": "Pet not found"},
    405: {"description": "Validation exception"},
}
@router.put(
    "/pet",
    responses=responses_update_pet,
    tags=["pet"],
    summary="Update an existing pet",
)
async def update_pet(
    pet: Pet = Body(None, description="Pet object that needs to be added to the store"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> Pet:
    
    return processor.update_pet(
        pet,
        token_petstore_auth,
    )



# update_pet_with_form ########################################################################
responses_update_pet_with_form: response_type = {
    405: {"description": "Invalid input"},
}
@router.post(
    "/pet/{petId}",
    responses=responses_update_pet_with_form,
    tags=["pet"],
    summary="Updates a pet in the store with form data",
)
async def update_pet_with_form(
    petId: int = Path(None, description="ID of pet that needs to be updated"),
    name: str = Form(None, description="Updated name of the pet"),
    status: str = Form(None, description="Updated status of the pet"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> None:
    
    return processor.update_pet_with_form(
        petId,
        name,
        status,
        token_petstore_auth,
    )



# upload_file ########################################################################
responses_upload_file: response_type = {
    200: {"model": ApiResponse, "description": "successful operation"},
}
@router.post(
    "/pet/{petId}/uploadImage",
    responses=responses_upload_file,
    tags=["pet"],
    summary="uploads an image",
)
async def upload_file(
    petId: int = Path(None, description="ID of pet to update"),
    additional_metadata: str = Form(None, description="Additional data to pass to server"),
    file: str = Form(None, description="file to upload"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> ApiResponse:
    
    return processor.upload_file(
        petId,
        additional_metadata,
        file,
        token_petstore_auth,
    )
