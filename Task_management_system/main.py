from fastapi import FastAPI, HTTPException , Request
from schemas import TaskCreate,TaskUpdate
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app=FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
     request:Request,
     exc:RequestValidationError
):
     errors= []

     for error in exc.errors():

        field= error["loc"][-1]
        if error["type"] == "missing":
            if field == "title":
                errors.append("Title field cannot be empty")

            elif field == "completed":
                errors.append("Completed field cannot be empty")

            else:
                errors.append(error["msg"].replace("Value error," ,"").strip())

     return JSONResponse(
        status_code=400,
        content={
             "sucess": False,
             "message": "Validation Failed",
             "errors": errors
        }
      )



tasks = [
    {"id": 1, "title": "Learn Python", "completed": True},
    {"id": 2, "title": "Learn FastAPI", "completed": False},
    {"id": 3, "title": "Learn Java", "completed": False},
    {"id": 4, "title": "learn Python project", "completed": False},
    {"id": 5, "title": "learn Java project", "completed": False},
    {"id": 6, "title": "Build React project", "completed": False},
    {"id": 7, "title": "Build Dotnet project", "completed": False},
]


@app.get("/tasks")
def get_tasks(
    search : str = None,
    completed : bool =None ,
    page :int =1,
    limit: int =2,
    sort:str = "id",
    order:str = "asc"
):
        if search :
                tasks_result = [
                    task
                    for task in tasks
                    if search.lower() in task["title"].lower() 
                ]
        else:
            tasks_result = tasks

        if completed is not None:
                tasks_result = [
                    task
                    for task in tasks_result
                    if task["completed"] == completed
                ]

                if order == "desc":
                    tasks_result = sorted(
                        tasks_result,
                        key=lambda task:task[sort],
                        reverse=True
                    )
                tasks_result = sorted(
                    tasks_result,
                    key=lambda task:task[sort]
                )
  
        start = (page-1)*limit
        end = start + limit
        return tasks_result[start:end]
        

@app.get("/api/tasks")
def get_without_filters():
     return tasks

@app.get("/tasks/{task_id}")
def get_one(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
             return task

    raise HTTPException(
        status_code=404,
        detail="item not found"
    )

@app.post("/tasks",status_code=201)

def create_task(task:TaskCreate):
    try:
        new_task={
            "id": len(tasks) + 1,
            "title": task.title,
            "completed": task.completed
            
        }
        tasks.append(new_task)
        
        return new_task

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong"
        )

@app.put("/tasks/{task_id}")
def update_task(task_id : int ,updated_task:TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"]=updated_task.title
            task["completed"]=updated_task.completed
            return task
    raise HTTPException(
            status_code=404,  
            detail="item not found"
        )

@app.patch("/tasks/{task_id}")
def update_task(task_id:int, updated_task:TaskUpdate):
     for task in tasks:
          if task["id"] == task_id:
            if updated_task.title is not None:
               task["title"]= updated_task.title
            if updated_task.completed is not None:
               task["completed"]=updated_task.completed

            return task
     raise HTTPException(
          status_code=404,
          detail="item not found"
     )


@app.delete("/tasks/{tasks_id}")
def delete_task(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message":"Deleted"}






# @app.get("/tasks")
# def get_tasks(search: str = None):
#     if search:
#         return[
#             task
#             for task in tasks
#             if search.lower() in task["title"].lower()
#         ]
#     return tasks

# @app.get("/tasks")
# def get_tasks(completed:bool = None):
#     if completed is not None:
#         return[
#             task
#             for task in tasks
#             if task["completed"] == completed
#         ]
#     return tasks

# @app.get("/tasks")
# def get_tasks(page:int =1,limit:int =2):

#     start = (page-1)*limit
#     end = start + limit
#     return tasks[start:end]

# @app.get("/tasks")
# def get_tasks(sort: str = id, order:str ="asc"):
#     if order == "desc":
#         return sorted(tasks, key = lambda task:task[sort], reverse=True)
#     return sorted(tasks, key=lambda task :task[sort])
