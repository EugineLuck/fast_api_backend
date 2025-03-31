from sqlalchemy.orm import Session
from app.repositories.system_users_repository import SystemUsersRepository
from app.schemas.system_users_schema import SystemUserSchema

class SystemUsersService:
    def __init__(self, db: Session):
        self.repository = SystemUsersRepository(db)

    def create_user(self, user_data: dict):
        return self.repository.create_user(user_data)

    def get_user_by_id(self, user_id: int):
        return self.repository.get_user_by_id(user_id)

    def update_user(self, user_id: int, user_data: dict):
        return self.repository.update_user(user_id, user_data)

    def delete_user(self, user_id: int):
        return self.repository.delete_user(user_id)