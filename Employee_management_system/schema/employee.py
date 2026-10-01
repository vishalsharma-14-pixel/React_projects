from pydantic import BaseModel , EmailStr, field_validator,Field
from datetime import datetime



 
class DepartmentResponse(BaseModel):
    id: int
    name: str

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: DepartmentResponse
    salary: float
    is_active: bool
    create_date: datetime


class CreateEmployee(BaseModel):
    name:str = Field(min_length=3,max_length=20)
    email:EmailStr
    salary:float 
    is_active: bool = True
    department_id: int

    @field_validator("name",mode="before")
    @classmethod
    def validate_name(cls,value):
        if not value or value == "":
            raise ValueError("name cannot be empty")
        return value
    
    @field_validator("salary",mode="before")
    @classmethod
    def validate_salary(cls,value):
        if value == 0:
            raise ValueError("salary cannot be empty")
        return value
    
    @field_validator("department_id", mode="before")
    @classmethod
    def validate_department_id(cls, value):
        if value is None or value == "":
            raise ValueError("department_id cannot be empty")

        return value
    
    @field_validator("is_active",mode="before")
    @classmethod
    def validate_active(cls,value):
        if value == "":
            raise ValueError("is_active cannot be empty")
        elif value  not in [False,True,None]:
            raise ValueError("is_active must be true or false")
        return value

class UpdateEmployee(CreateEmployee):
    pass