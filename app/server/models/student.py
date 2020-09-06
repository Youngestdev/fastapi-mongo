from pydantic import BaseModel, EmailStr, Field


class StudentModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(...)
    gpa: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0"
            }
        }


class UpdateName(BaseModel):
    fullname: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez"
            }
        }


class UpdateEmail(BaseModel):
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@y.edu.ng"
            }
        }


class UpdateCourse(BaseModel):
    course: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "course": "Civil engineering"
            }
        }


class UpdateYear(BaseModel):
    year: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "year": 4
            }
        }


class UpdateGpa(BaseModel):
    gpa: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "gpa": "5.0"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
