from pydantic import BaseModel, Field , field_validator
from typing import Optional , Union


class TaskBase(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    completed: bool | None = False

    @field_validator("title",mode="before")
    @classmethod
    def validate_title(cls,value):
        if not value or value == "":
            raise ValueError("title cannot be empty")
        return value

    @field_validator("completed",mode="before")
    @classmethod
    def validate_completed(cls,value):
        if value == "":
            raise ValueError("completed cannot be empty")
        elif value  not in [False,True,None]:
            raise ValueError("completed must be true or false")
        return value


class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

