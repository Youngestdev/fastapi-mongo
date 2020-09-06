from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.database import *
from app.server.models.student import *

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


@router.put("/name/{id}")
async def update_name(id: str, req: UpdateName = Body(...)):
    updated_student = await update_student_name(id, req.fullname)
    return ResponseModel("Student with ID: {} name update is successful".format(id),
                         "Student name updated succeasfully") \
        if updated_student \
        else ErrorResponseModel("An error occured", 404, "Student with id {0} doesn't exist.".format(id))


@router.put("/email/{id}")
async def update_email(id: str, req: UpdateEmail = Body(...)):
    updated_email = await update_student_email(id, req.email)
    return ResponseModel("Student with ID: {} email update is successful".format(id),
                         "Student email updated succeasfully") \
        if updated_email \
        else ErrorResponseModel("An error occured", 404, "Student with id {0} doesn't exist.".format(id))


@router.put("/course/{id}")
async def update_course(id: str, req: UpdateCourse = Body(...)):
    updated_course = await update_student_course(id, req.course)
    return ResponseModel("Student with ID: {} course update is successful".format(id),
                         "Student course updated succeasfully") \
        if updated_course \
        else ErrorResponseModel("An error occured", 404, "Student with id {0} doesn't exist.".format(id))


@router.put("/year/{id}")
async def update_year(id: str, req: UpdateYear = Body(...)):
    updated_year = await update_student_year(id, req.year)
    return ResponseModel("Student with ID: {} year update is successful".format(id),
                         "Student year updated succeasfully") \
        if updated_year \
        else ErrorResponseModel("An error occured", 404, "Student with id {0} doesn't exist.".format(id))


@router.put("/gpa/{id}")
async def update_gpa(id: str, req: UpdateGpa = Body(...)):
    updated_gpa = await update_student_gpa(id, req.gpa)
    return ResponseModel("Student with ID: {} GPA update is successful".format(id),
                         "Student GPA updated succeasfully") \
        if updated_gpa \
        else ErrorResponseModel("An error occured", 404, "Student with id {0} doesn't exist.".format(id))
