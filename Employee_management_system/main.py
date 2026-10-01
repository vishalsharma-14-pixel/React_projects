from fastapi import FastAPI,Depends,HTTPException,Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from services.employee_service import (get_employee_by_id, get_all_employees, create_employee, delete_employee, update_employee)
from schema.employee import EmployeeResponse,CreateEmployee,UpdateEmployee

app = FastAPI()
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = []

    for error in exc.errors():

        field = error["loc"][-1]

        if error["type"] == "missing":

            if field == "name":
                errors.append("Name field cannot be empty")

            elif field == "email":
                errors.append("Email field cannot be empty")

            elif field == "department":
                errors.append("Department field cannot be empty")

            elif field == "salary":
                errors.append("Salary field cannot be empty")

            elif field == "is_active":
                errors.append("IsActive field cannot be empty")

            else:
                errors.append(error["msg"])

        else:
            errors.append(
                error["msg"].replace("Value error,", "").strip()
            )

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": "Validation Failed",
            "errors": errors
        }
    )

@app.get("/")
def home():
    return{
        "message":"APi is running"
    }

@app.get("/employees",response_model=list[EmployeeResponse])
def get_employees():

    employees = get_all_employees()
    if not employees:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
            )
    return employees

@app.get("/employees/{id}",response_model=EmployeeResponse)
def get_employee(id:int ):

    employee= get_employee_by_id(id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    return employee

@app.post("/employees",status_code=201,response_model=EmployeeResponse)
def create_employee_id(employee:CreateEmployee):
    return create_employee(employee)

@app.put("/employee/{id}",response_model=EmployeeResponse)
def update_employee_id(id:int ,employee:UpdateEmployee):

    try:
        updated_employee= update_employee(
            id,
            employee
        )

        if updated_employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not Found"
            )

        return updated_employee

    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )
    

@app.delete("/employees/{id}")
def delete_employee_id(id:int):

    employee= delete_employee(id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message":"Employee deleted"
    }


