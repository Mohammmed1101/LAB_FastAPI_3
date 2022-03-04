from database import Base
from sqlalchemy import String, Float, Integer, Column, Text , ForeignKey
from sqlalchemy.orm import relationship

class Student(Base): 
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    student_F_Name = Column(String(50), nullable=False)
    student_L_Name = Column(String(50), nullable=False)
    gpa = Column(Float, nullable=False)
    # course_id = Column(Integer, ForeignKey("course_id"))

    course = relationship("Course", back_populates="student")

    def __repr__(self):
        return f"<Item student_F_Name={self.student_F_Name} gpa={self.gpa}>"




class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True,index=True)
    course_name = Column(String(50), nullable=False)
    course_hours = Column(String(50), nullable=False)
    course_description = Column(Text, nullable=False)
    students = Column(Integer, ForeignKey("s_id"))
    
    student = relationship("Student", back_populates="course")