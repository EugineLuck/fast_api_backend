from typing import Optional
from sqlalchemy.orm import Session
from app.schemas.customer_schema import CustomerSchema  # Ensure correct import
from app.models.customer import Customer  


class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db  # Use SQLAlchemy session
        self.customers = []
        self.counter = 1

    def create(self, name, prefix="cust-2025"):
        if not isinstance(name, str):
            raise ValueError("Customer name must be a string")  # Ensure name is a string

        # Query the database to find the highest unique_id
        last_customer = self.db.query(Customer).order_by(Customer.id.desc()).first()
        last_counter = int(last_customer.unique_id.split("/")[-1]) if last_customer else 0
        unique_id = f"{prefix}/{last_counter + 1:03}"

        # Create a new Customer instance
        customer = Customer(name=name.strip(), unique_id=unique_id)  # Strip any extra spaces
        self.db.add(customer)  # Add to the session
        self.db.commit()  # Commit to persist in the database
        self.db.refresh(customer)  # Refresh to get the updated instance

        # Return a schema representation of the customer
        return CustomerSchema(name=customer.name, unique_id=customer.unique_id)

    def read(self, customer_id):
        for customer in self.customers:
            if customer["id"] == customer_id:
                return customer
        return None

    def update(self, customer_id, name):
        for customer in self.customers:
            if customer["id"] == customer_id:
                customer["name"] = name
                return customer
        return None

    def delete(self, customer_id):
        for index, customer in enumerate(self.customers):
            if customer["id"] == customer_id:
                del self.customers[index]
                return True
        return False
