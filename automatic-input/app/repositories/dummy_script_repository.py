import random

from sqlalchemy.orm import Session

from app.types.e_attack import EAttack
from app.models.dummy_script_model import DummyScriptModel
from app.utils.custom_logger import CustomLogger


class DummyScriptRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.logger = CustomLogger()

    def find_random_by_attack_type(self, attack_type: EAttack):
        scripts = self.session.query(DummyScriptModel).filter_by(attack_type=attack_type).all()

        if not scripts:
            self.logger.error(f'No scripts for attack type: {attack_type}')
            return None

        try:
            return random.choice(scripts)
        except IndexError as e:
            self.logger.error(f'Error selecting random script: {e}')
            return None

    def find_random(self):
        scripts = (self.session.query(DummyScriptModel)
                   .filter(DummyScriptModel.attack_type != EAttack.WEB_ATTACK_SQL_INJECTION).all())

        if not scripts:
            self.logger.error(f'No scripts for this type')
            return None

        try:
            return random.choice(scripts)
        except IndexError as e:
            self.logger.error(f'Error selecting random script: {e}')
            return None
