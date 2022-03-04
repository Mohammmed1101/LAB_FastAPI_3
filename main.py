from fastapi import FastAPI , status

from typing import List
from database import SessionLocal
import schemas
from routers import student , course

db=SessionLocal()
app = FastAPI()
app.include_router(student.router)
app.include_router(course.router)


@app.get('/students',response_model=List[schemas.showStudent],status_code=status.HTTP_201_CREATED)
def get_all():
    return student.get_all_students()

@app.get('/students/{student_id}',response_model=schemas.Student)
def get_an_student(student_id:int):
    return student.get_all_students(student_id)

@app.post('/students', response_model=schemas.Student, status_code=status.HTTP_201_CREATED)
def create_an_student(req: schemas.Student):
    return student.create_an_student(req)

@app.put('/student/{student_id}',response_model=schemas.Student,status_code=status.HTTP_200_OK)
def update_an_student(student_id:int,students:schemas.Student):
    return student.update_an_student(student_id,students)


@app.delete('/student/{student_id}')
def delete_student(student_id:int):
    return student.delete_student(student_id)




@app.get('courses',response_model=List[schemas.showCourse],status_code=status.HTTP_201_CREATED)
def get_all_courses():
    return course.get_all_courses()


@app.post('/courses' , response_model=schemas.Course , status_code=status.HTTP_201_CREATED)
def create_an_courses(req:schemas.Course):
    return course.create_an_courses(req)

    