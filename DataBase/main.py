from models import Student
from sqlalchemy import engine
from sqlalchemy.orm import session
from connection import Connection 
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.sql import table , insert 

engine = Connection.get_connection()
session = Connection.create_session()

metadata = MetaData(bind=engine)
student = table("student" , metadata , autoload=True)

i = insert(student)
i = i.values({"name" : "mahdi" , "family" : "kaseb" , "grade" : 99 })
session.execute(i)