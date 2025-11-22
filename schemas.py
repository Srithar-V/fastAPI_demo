from pydantic import BaseModel, Field

''' todo-list API data validation '''
class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    
# Schema used when creating a new todo (NO id)
class TodoCreate(TodoBase):
    pass

# Schema used when returning a todo (WITH id)
class Todo(TodoBase):
    id: int

    model_config = {   # class-object to dictionary data type for validation
        "from_attributes": True
    }


''' bio-data API data validation '''
class BioDataBase(BaseModel):
    name: str
    mobile: str = Field(pattern=r"^[6-9][0-9]{9}$")
    
class BioDataCreate(BioDataBase):
    pass

class BioData(BioDataBase):
    id: int

    model_config = {  # class-object to dictionary data type for validation
        "from_attributes": True
    }
    