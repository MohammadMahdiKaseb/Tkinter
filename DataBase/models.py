
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , String , INTEGER , DateTime, engine
from sqlalchemy.sql.sqltypes import Integer
from connection import Connection


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    studenId = Column(INTEGER() , primary_key=True , autoincrement=True)
    name = Column(String(50))
    family = Column(String(50))
    grade = Column(Integer)
    created_at = Column(DateTime())



    def __init__(self , name = None , family = None , grade = None ):
     self.name = name
     self.family = family 
     self.grade = grade



engine = Connection().get_connection()
if not engine.dialect.has_table(engine , "student"): 
    Base.metadata.create_all(engine , checkfirst=True )
    print("Database Created")
else:
    print("Database {} exists!".format("student")) 


