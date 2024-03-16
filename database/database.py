# from typing import List, Union

# from beanie import PydanticObjectId

# from models.User import User
# from models.Category import Category

# user_collection = User
# category_collection = Category


# async def add_user(new_user: User) -> User:
#     user = await new_user.create()
#     return user


# async def retrieve_students() -> List[Student]:
#     students = await student_collection.all().to_list()
#     return students


# async def add_student(new_student: Student) -> Student:
#     student = await new_student.create()
#     return student


# async def retrieve_student(id: PydanticObjectId) -> Student:
#     student = await student_collection.get(id)
#     if student:
#         return student


# async def delete_student(id: PydanticObjectId) -> bool:
#     student = await student_collection.get(id)
#     if student:
#         await student.delete()
#         return True


# async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
#     des_body = {k: v for k, v in data.items() if v is not None}
#     update_query = {"$set": {field: value for field, value in des_body.items()}}
#     student = await student_collection.get(id)
#     if student:
#         await student.update(update_query)
#         return student
#     return False
