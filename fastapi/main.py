from fastapi import FastAPI,Depends 
from sqlalchemy.orm import Session
from database import engine , SessionLocal
from schemas import TaskCreate , TaskUpdate
import models 


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {
                "message": "Task API is running"

    }

@app.get("/tasks")
def get_all_tasks(db : Session = Depends(get_db)):
    db_tasks = db.query(models.Task).all()

    return db_tasks






    





# @app.get("/tasks/{task_id}")

# def get_task(task_id:int):

#     for task in tasks:
#         if(task["id"]==task_id):
#             return task

#     raise HTTPException(
#         status_code=404,
#         detail="Task not found"
#     )

# @app.post("/tasks",status_code=201)
# def create_task(task : Task):

#     new_task= {
#             "id": len(tasks) + 1,
#             "title": task.title,
#             "completed":task.completed
#     }
  
#     tasks.append(new_task)

#     return new_task

# @app.put("/tasks/{task_id}")

# def update_task(task_id :int, updated_task:TaskUpdate):

#     for task in tasks:
#         if task["id"] == task_id:
#             task["title"] = updated_task.title
#             task["completed"] = updated_task.completed

#             return task

#     raise HTTPException(
#         status_code=404,
#         detail="Task not found"
#     )


# @app.patch("/tasks/{task_id}")
# def patch_task(task_id:int , updated_task:TaskPatch):

#     for task in tasks:
#         if task["id"] == task_id:
#             if updated_task.title is not None:
#                 task["title"]=updated_task.title
#             if updated_task.completed is not None:
#                 task["completed"]=updated_task.completed

#             return task
        
#     raise HTTPException(
#         status_code=404,
#         detail="Task not found"
#     )


# @app.delete("/tasks/{task_id}",status_code=204)
# def delete_task(task_id:int ):

#     for task in tasks:
#         if task["id"]==task_id:
#             tasks.remove(task)
#             return
