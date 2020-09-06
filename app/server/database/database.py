import motor.motor_asyncio
from bson import ObjectId
from decouple import config

from app.server.database.database_helper import student_helper

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection('students_collection')


async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_student_name(id: str, fullname: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one({"_id": ObjectId(id)}, {"$set": {"fullname": fullname}})
        return True


async def update_student_email(id: str, email: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one({"_id": ObjectId(id)}, {"$set": {"email": email}})
        return True


async def update_student_course(id: str, course: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one({"_id": ObjectId(id)}, {"$set": {"course": course}})
        return True


async def update_student_year(id: str, year: int):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one({"_id": ObjectId(id)}, {"$set": {"year": year}})
        return True


async def update_student_gpa(id: str, gpa: float):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one({"_id": ObjectId(id)}, {"$set": {"gpa": gpa}})
        return True
