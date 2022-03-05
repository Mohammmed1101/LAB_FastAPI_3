
from fastapi import APIRouter , HTTPException , status
from typing import List
import schemas , main  ,models

router = APIRouter()


@router.get('/students',response_model=List[schemas.Student],status_code=status.HTTP_201_CREATED , tags=["Students"])
def get_all_students():
    students=main.db.query(models.Student).all()
    return students

@router.get('/students/{student_id}',response_model=schemas.Student , tags=["Students"])
def get_an_student(student_id:int):
    student = main.db.query(models.Student).filter(models.Student.student_id==student_id).first()
    return student

@router.post('/students', response_model=schemas.Student, status_code=status.HTTP_201_CREATED ,  tags=["Students"])
def create_an_student(req: schemas.Student):
    db_student = main.db.query(models.Student).filter(models.Student.student_F_Name == req.student_F_Name).first()
    if db_student is not None:
        raise HTTPException(status_code=400, detail="Student already exists")

    new_student = models.Student(
    student_F_Name=req.student_F_Name,
    student_L_Name=req.student_L_Name,
    gpa=req.gpa,
    course_id=req.course_id )

    main.db.add(new_student)
    main.db.commit()
    return new_student

@router.put('/student/{student_id}',response_model=schemas.Student,status_code=status.HTTP_200_OK ,  tags=["Students"])
def update_an_student(student_id:int,students:schemas.Student):
    student_to_update=main.db.query(models.Student).filter(models.Student.student_id==student_id).first()
    student_to_update.student_F_Name=students.student_F_Name
    student_to_update.student_L_Name=students.student_L_Name
    student_to_update.gpa=students.gpa
    
    main.db.commit()
    return student_to_update


@router.delete('/student/{student_id}' , tags=["Students"])
def delete_student(student_id:int):
    student_to_delete=main.db.query(models.Student).filter(models.Student.student_id==student_id).first()

    if student_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")

    main.db.delete(student_to_delete)
    main.db.commit()
    return student_to_delete
