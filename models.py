from sqlalchemy import Column, Integer, String, Boolean
from database import Base
# table 1
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    
# table 2
class BioData(Base):
    __tablename__ = "biodata"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mobile = Column(String, nullable=False) 