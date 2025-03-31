from fastapi import APIRouter, HTTPException, Depends
from app.schemas.system_users_schema import SystemUserSchema
from app.services.system_users_service import SystemUsersService
from app.models.base import get_db
from sqlalchemy.orm import Session

router = APIRouter()

class SystemUsersController:
    @router.post("/users/", response_model=SystemUserSchema)
    def create_user(user: SystemUserSchema, db: Session = Depends(get_db)):
        service = SystemUsersService(db)
        new_user = service.create_user(user.dict())
        return new_user

    @router.get("/users/{user_id}", response_model=SystemUserSchema)
    def read_user(user_id: int, db: Session = Depends(get_db)):
        service = SystemUsersService(db)
        user = service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @router.put("/users/{user_id}", response_model=SystemUserSchema)
    def update_user(user_id: int, user: SystemUserSchema, db: Session = Depends(get_db)):
        service = SystemUsersService(db)
        updated_user = service.update_user(user_id, user.dict())
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user

    @router.delete("/users/{user_id}", response_model=dict)
    def delete_user(user_id: int, db: Session = Depends(get_db)):
        service = SystemUsersService(db)
        success = service.delete_user(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return {"detail": "User deleted successfully"}