from pydantic import BaseModel

class Student(BaseModel):
    student_id:int
    student_F_Name:str
    student_L_Name:str
    gpa:float
    

    class Config: 
        orm_mode=True

class Course(BaseModel):
    course_id:int
    course_name:str
    course_hours:str
    course_description:str
    

    class Config: 
        orm_mode=True

class showCourse(BaseModel):
    course_id:int
    course_name:str
    course_hours:str
    course_description:str
    student:Student

    class Config: 
        orm_mode=True

class showStudent(BaseModel):
    course_id:int
    course_name:str
    course_hours:str
    course_description:str
    course : Course
    
    class Config: 
        orm_mode=True
