from schema.employee import EmployeeResponse,DepartmentResponse

def employee_form_row(row):
    return EmployeeResponse(
        id=row.Id,
        name=row.Name,
        email=row.Email,

        department=DepartmentResponse(
            id=row.DepartmentId,
            name=row.DepartmentName
        ),

        salary=row.Salary,
        is_active=row.IsActive,
        create_date=row.CreateDate
    )

