from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subjects")

class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    score = Column(Float)
    date = Column(DateTime)

    student = relationship("Student", back_populates="scores")
    subject = relationship("Subject", back_populates="scores")

Student.scores = relationship("Score", back_populates="student")
Subject.scores = relationship("Score", back_populates="subject")
Teacher.subjects = relationship("Subject", back_populates="teacher")
