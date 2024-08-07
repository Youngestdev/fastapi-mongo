from fastapi import APIRouter, Body

from database.database import *
from models.contact import Contact
from schemas.contact import Response, UpdateContactModel


router = APIRouter()


@router.get("/", response_description="Contacts retrieved", response_model=Response)
async def get_contacts():
    contacts = await retrieve_contacts()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Contacts data retrieved successfully",
        "data": contacts,
    }


@router.get("/{id}", response_description="Contacts data retrieved", response_model=Response)
async def get_contact_data(id: PydanticObjectId):
    contact = await retrieve_contact(id)
    if contact:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Contact data retrieved successfully",
            "data": contact,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Contact doesn't exist",
    }


@router.post(
    "/",
    response_description="Contact data added into the database",
    response_model=Response,
)
async def add_contact_data(contact: Contact = Body(...)):
    new_contact = await add_contact(contact)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Contact created successfully",
        "data": new_contact,
    }


@router.delete("/{id}", response_description="Contact data deleted from the database")
async def delete_contact_data(id: PydanticObjectId):
    deleted_contact = await delete_contact(id)
    if deleted_contact:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Contact with ID: {} removed".format(id),
            "data": deleted_contact,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Contact with id {0} doesn't exist".format(id),
        "data": False,
    }


@router.put("/{id}", response_model=Response)
async def update_contact(id: PydanticObjectId, req: UpdateContactModel = Body(...)):
    updated_contact = await update_contact_data(id, req.dict())
    if updated_contact:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Contact with ID: {} updated".format(id),
            "data": updated_contact,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Contact with ID: {} not found".format(id),
        "data": False,
    }
