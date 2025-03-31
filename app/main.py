from fastapi import FastAPI
from app.controllers.system_users_controller import router as system_users_router
from app.controllers.customer_controller import router as customer_router
from app.models.base import Base, engine  # Updated import

app = FastAPI()

def init_db():
    try:
        Base.metadata.create_all(bind=engine)  # Use the engine from base.py
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Database initialization error: {e}")

@app.on_event("startup")
async def startup_event():
    # Async startup logic
    init_db()

@app.on_event("shutdown")
async def shutdown_event():
    # Add any cleanup logic here if needed
    print("Application is shutting down...")

# Include routers
app.include_router(system_users_router, prefix="/users", tags=["System Users"])
app.include_router(customer_router, prefix="/customers", tags=["Customers"])
