from fastapi import APIRouter , HTTPException , status
from typing import List
import schemas , main  ,models

router = APIRouter()

@router.get('courses',response_model=List[schemas.Course],status_code=status.HTTP_201_CREATED , tags=["Courses"])
def get_all_courses():
    courses_db = main.db.query(models.Course).all

    return courses_db


@router.post('/courses' , response_model=schemas.Course , status_code=status.HTTP_201_CREATED , tags=["Courses"])
def create_an_courses(req:schemas.Course):
    db_course = main.db.query(models.Course).first()
    if db_course is not None:
        raise HTTPException(status_code=400, detail="Course already exists")
    
    new_course = models.Course(
        course_name=req.course_name,
        course_hours=req.course_hours,
        course_description=req.course_description,
        student_id = 1)
    
    main.db.add(new_course)
    main.db.commit()

    return new_course