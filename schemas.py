from pydantic import BaseModel



class Student(BaseModel):
    student_id:int
    student_F_Name:str
    student_L_Name:str
    gpa:float
    course_id:int
    
    class Config: 
        orm_mode=True

class Course(BaseModel):
    course_id:int
    course_name:str
    course_hours:str
    course_description:str
    student_id:int

    class Config: 
        orm_mode=True

class showCourse(BaseModel):
    course_id:int
    course_name:str
    course_hours:str
    course_description:str
    student_id:int
    student:Student


    class Config: 
        orm_mode=True

class showStudent(BaseModel):
    student_id:int
    student_F_Name:str
    student_L_Name:str
    gpa:float
    course_id : Course
    course_id:int

    course:Course
    
    class Config: 
        orm_mode=True
