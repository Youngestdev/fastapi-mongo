from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.database import retrieve_students, add_student, retrieve_student, delete_student, update_student_data
from app.server.models.student import StudentModel, ResponseModel, ErrorResponseModel

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
        else ErrorResponseModel("An error occured.", 404, "Student doesn'exist.")


@router.post("/new", response_description="Student data added into the database")
async def add_student_data(student: StudentModel = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")


# I will have to write multiple for this tbh.
@router.put("/{id}", response_description="Student data updated")
async def update_student(id: str, body: StudentModel = Body(...)):
    student_data = jsonable_encoder(body)
    updated_student = await update_student_data(id, student_data)
    return ResponseModel(updated_student, "")


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    return ResponseModel("Student with ID: {} removed".format(id), "Student deleted successfully") \
        if deleted_student \
        else ErrorResponseModel("An error occured", 404, "Student with id {0} doesn't exist".format(id))
