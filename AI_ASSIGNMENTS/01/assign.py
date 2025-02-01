from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentModel(BaseModel):
    name: str
    email: str
    age: int
    courses: str


@app.get("/students/{student_id}")
async def get_student_info(
    student_id: int,
    include_grades: bool,
    courses: str
):
    student_info = {"student_id": student_id,
                    "include_grades": include_grades, "courses": courses}
    return student_info
