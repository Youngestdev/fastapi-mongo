from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.student import *

router = APIRouter()


@router.get("/", response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    return ResponseModel(students, "Students data retrieved successfully") \
        if len(students) > 0 \
        else ResponseModel(
        students, "Empty list returned")


@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id):
    student = await retrieve_student(id)
    return ResponseModel(student, "Student data retrieved successfully") \
        if student \
        else ErrorResponseModel("An error occured.", 404, "Student doesn't exist.")


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentModel = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    return ResponseModel("Student with ID: {} removed".format(id), "Student deleted successfully") \
        if deleted_student \
        else ErrorResponseModel("An error occured", 404, "Student with id {0} doesn't exist".format(id))


@router.put("{id}")
async def update_student(id: str, req: UpdateStudentModel = Body(...)):
    updated_student = await update_student_data(id, req.dict())
    return ResponseModel("Student with ID: {} name update is successful".format(id),
                         "Student name updated successfully") \
        if updated_student \
        else ErrorResponseModel("An error occurred", 404, "There was an error updating the student.".format(id))
