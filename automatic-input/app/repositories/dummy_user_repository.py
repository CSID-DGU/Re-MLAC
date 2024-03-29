import random

from sqlalchemy.orm import Session

from app.types.e_attack import EAttack
from app.utils.custom_logger import CustomLogger
from app.models.dummy_user_model import DummyUserModel


class DummyUserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.logger = CustomLogger()

    def find_by_attack_type(self, attack_type: EAttack):
        users = self.session.query(DummyUserModel).filter_by(attack_type=attack_type).all()

        if not users:
            self.logger.error(f'No users found for attack type: {attack_type}')
            return None

        try:
            return random.choice(users)
        except IndexError as e:
            self.logger.error(f'Error selecting random user: {e}')
            return None

