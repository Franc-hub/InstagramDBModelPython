import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , Boolean , Table 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)
    promo = Column(Boolean(), unique=False, nullable=False)
    img = Column(String(250), unique=True, nullable=False)
    school_id = Column(Integer, ForeignKey('school.id'))
    school = relationship("School", back_populates="student")
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship("Teacher", back_populates="student")


class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False, nullable=False)
    img = Column(String(250), unique=True, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'))
    students = relationship("student", back_populates="school")


    
class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    type_of_teacher = Column(String(80), unique=False, nullable=False)
    linkedin = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)
    promo = Column(Boolean(), unique=False, nullable=False)
    img = Column(String(250), unique=True, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship("Student", back_populates="student")
    school_id = Column(Integer, ForeignKey('school.id'))
    school = relationship("School", back_populates="teacher")


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    dynamsim = Column(Integer())
    pasion = Column(Integer())
    practises_example = Column(Integer())
    near = Column(Integer())
    # date_teacher = Column(DateTime, default=datetime.datetime.utcnow)
    more_info = Column(String(500), unique=False, nullable=True)
    gif = Column(String(50), unique=False, nullable=True)



class Review_teacher(Base):
    __tablename__ = 'review_teacher'
    id = Column(Integer, primary_key=True)



class Review_school(Base):
    __tablename__ = 'review_school'
    id = Column(Integer, primary_key=True)


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e