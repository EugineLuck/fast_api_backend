from sqlalchemy.orm import Session
from app.models.system_users import SystemUser
from app.schemas.system_users_schema import SystemUserSchema

class SystemUsersRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: dict) -> SystemUser:
        user_obj = SystemUserSchema(**user)
        new_user = SystemUser(username=user_obj.username, password=user_obj.password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_id(self, user_id: int) -> SystemUser:
        return self.db.query(SystemUser).filter(SystemUser.id == user_id).first()

    def update_user(self, user_id: int, user: SystemUserSchema) -> SystemUser:
        existing_user = self.get_user_by_id(user_id)
        if not existing_user:
            return None
        existing_user.username = user.username
        existing_user.password = user.password
        self.db.commit()
        self.db.refresh(existing_user)
        return existing_user

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True
