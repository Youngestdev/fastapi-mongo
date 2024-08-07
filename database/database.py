from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.contact import Contact

admin_collection = Admin
contact_collection = Contact


async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin




###################

async def retrieve_contacts() -> List[Contact]:
    contacts = await contact_collection.all().to_list()
    return contacts


async def add_contact(new_contact: Contact) -> Contact:
    contact = await new_contact.create()
    return contact


async def retrieve_contact(id: PydanticObjectId) -> Contact:
    contact = await contact_collection.get(id)
    if contact:
        return contact


async def delete_contact(id: PydanticObjectId) -> bool:
    contact = await contact_collection.get(id)
    if contact:
        await contact.delete()
        return True


async def update_contact_data(id: PydanticObjectId, data: dict) -> Union[bool, Contact]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    contact = await contact_collection.get(id)
    if contact:
        await contact.update(update_query)
        return contact
    return False
