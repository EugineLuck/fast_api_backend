from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.customer_schema import CustomerSchema
from app.services.customer_service import CustomerService
from app.models.base import get_db 

router = APIRouter()

@router.post("/customers", response_model=CustomerSchema)
def create_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
    if not isinstance(customer.name, str) or not customer.name.strip():
        raise HTTPException(status_code=400, detail="Invalid customer name")
    service = CustomerService(db)
    return service.create_customer(customer)

@router.get("/customers/{customer_id}", response_model=CustomerSchema)
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    service = CustomerService(db)
    customer = service.get_customer_by_id(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/customers/{customer_id}", response_model=CustomerSchema)
def update_customer(customer_id: str, customer: CustomerSchema, db: Session = Depends(get_db)):
    service = CustomerService(db)
    updated_customer = service.update_customer(customer_id, customer)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/customers/{customer_id}", response_model=bool)
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    service = CustomerService(db)
    success = service.delete_customer(customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
    return success