from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import Todo, BioData
from schemas import (
    TodoCreate, Todo as TodoSchema,
    BioDataCreate, BioData as BioDataSchema
)

app = FastAPI()

# Initialize database tables
init_db()

def common_post_api_response(res = None, message = "data created successfully..!"):
    return { "data": { "id": res.id }, "message": message }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def healthCheck():
    return {"message": "API is working now!"}


''' ------------ TODO APIs ---------------- '''

@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())
    print("````````````````````````TODO payload:`````````````````````````````", todo, todo.dict(), db_todo)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return common_post_api_response(db_todo, "todo created successfully..!")


@app.get("/todos", response_model=list[TodoSchema])
def get_all_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()


@app.get("/todos/{todo_id}", response_model=list[TodoSchema])
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.delete("/todo_delete/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return { "message": "todo deleted successfully..!" }



''' ------------ BIO DATA APIs ---------------- '''

@app.post("/bio_data", response_model=BioDataSchema)
def create_bio_data(bio: BioDataCreate, db: Session = Depends(get_db)):
    db_bio = BioData(**bio.dict())
    print("BioData payload:", bio, db_bio)
    db.add(db_bio)
    db.commit()
    db.refresh(db_bio)
    return db_bio


@app.get("/bio_data", response_model=list[BioDataSchema])
def get_all_bio_data(db: Session = Depends(get_db)):
    return db.query(BioData).all()
    
    



