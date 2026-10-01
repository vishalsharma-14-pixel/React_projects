from database.connection import get_connection
from database.procedures import GET_ALL_EMPLOYEES, GET_EMPLOYEE_BY_ID, CREATE_EMPLOYEE, DELETE_EMPLOYEE, UPDATE_EMPLOYEE
from models.employee import employee_form_row
import pyodbc

def get_employee_by_id(employee_id:int ):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            GET_EMPLOYEE_BY_ID,
            employee_id
        )

        row = cursor.fetchone()

        if not row:
            return None

        return(
            employee_form_row(row)
        )
    finally:
        cursor.close()
        connection.close()

def get_all_employees():

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(GET_ALL_EMPLOYEES)

        rows=cursor.fetchall()

        return[
            employee_form_row(row)
            for row in rows
        ]
    finally:
        cursor.close()
        connection.close()

def create_employee(employee):

    connection=get_connection()
    cursor=connection.cursor()

    try:
        cursor.execute(
            CREATE_EMPLOYEE,
            employee.name,
            employee.email,
            employee.department_id,
            employee.salary,
            employee.is_active,
        )
        while cursor.description is None:
            if not cursor.nextset():
                raise Exception("Stored procedure did not return an employee")

        row = cursor.fetchone()
        connection.commit()
        return employee_form_row(row)

    except pyodbc.IntegrityError:
        connection.rollback()
        raise ValueError("Employee with this email already exists")

    except:
        connection.rollback()
        raise   


    finally:
        cursor.close()
        connection.close()


def delete_employee(employee_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            DELETE_EMPLOYEE,
            employee_id
        )

        while cursor.description is None:
            if not cursor.nextset():
                raise Exception(
                    "Stored procedure did not return a result set"
                )

        row = cursor.fetchone()

        if row is None:
            connection.rollback()
            return False

        rows_deleted = row.RowsDeleted

        connection.commit()

        return rows_deleted > 0

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

def update_employee(employee_id, employee):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            UPDATE_EMPLOYEE,
            employee_id,         
            employee.name,       
            employee.email,      
            employee.department_id,
            employee.salary,     
            employee.is_active    
        )

        while cursor.description is None:
            if not cursor.nextset():
                raise Exception(
                    "Stored procedure did not return a result set"
                )

        row = cursor.fetchone()

        if row is None:
            connection.rollback()
            return None

        connection.commit()

        return employee_form_row(row)

    except pyodbc.IntegrityError as e:
        connection.rollback()
        print("DATABASE ERROR:", e)
        raise

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()