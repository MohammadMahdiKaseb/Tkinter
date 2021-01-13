from collections import namedtuple
from sqlalchemy.ext.declarative import base, declarative_base
from sqlalchemy import Column 


Base = declarative_base()


class Student(Base):

    __tablename__ = "student"
    studenId = Column()
    name = Column()
    family = Column()
    grade = Column()
    created_at = Column()

