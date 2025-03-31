from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer_schema import CustomerSchema

class CustomerService:
    def __init__(self, db):
        self.repository = CustomerRepository(db)

    def create_customer(self, customer: CustomerSchema):
        # Extract the name from the CustomerSchema object
        return self.repository.create(customer.name)

    def read_customer(self, customer_id):
        return self.repository.read(customer_id)

    def update_customer(self, customer_id, name):
        return self.repository.update(customer_id, name)

    def delete_customer(self, customer_id):
        return self.repository.delete(customer_id)