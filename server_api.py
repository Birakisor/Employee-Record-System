from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel, EmailStr
from datetime import date
import logging

from emp_database import AsyncSessionLocal, Employee

app = FastAPI()

logging.basicConfig(level=logging.INFO)

# Dependency for database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


class EmployeeSchema(BaseModel):
    name: str
    email: EmailStr
    department: str
    designation: str
    salary: float
    date_of_joining: date

# API Endpoint to receive employee data
@app.post("/employees/")
async def create_employee(employee: EmployeeSchema, db: AsyncSession = Depends(get_db)):
    try:
        # Check if email already exists
        result = await db.execute(select(Employee).filter(Employee.email == employee.email))
        existing_employee = result.scalars().first()
        if existing_employee:
            raise HTTPException(status_code=400, detail="Employee with this email already exists")
        
        # Create new employee record
        new_employee = Employee(
            name=employee.name,
            email=employee.email,
            department=employee.department,
            designation=employee.designation,
            salary=employee.salary,
            date_of_joining=employee.date_of_joining,
        )
        
        db.add(new_employee)
        await db.commit()
        return {"message": "Employee added successfully"}
    
    except Exception as e:
        logging.error(f"Error adding employee: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
