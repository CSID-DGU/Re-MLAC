from fastapi import HTTPException
from app.configs.data import DataFrameSingleton
from app.configs.database import SessionLocal
from app.utils.pandas_util import PandasUtil
from app.repositories.dummy_user_repository import DummyUserRepository
from app.repositories.dummy_script_repository import DummyScriptRepository
from app.schemas.packet_info_schema import PacketInfoSchema
import requests
import datetime
import os
from dotenv import load_dotenv

from app.utils.custom_logger import CustomLogger
from app.utils.label_util import LabelUtil

load_dotenv()


class PacketHandler:
    def __init__(self):
        self.dataframe_singleton = DataFrameSingleton()
        self.dummy_user_repository = DummyUserRepository(session=SessionLocal())
        self.dummy_script_repository = DummyScriptRepository(session=SessionLocal())
        self.logger = CustomLogger()
        self.label_util = LabelUtil()
        self.pandas_util = PandasUtil()
        self.packet_info_schema = PacketInfoSchema()
        self.url = os.getenv('POST_URL')

    def handle_request(self):
        random_row = self.dataframe_singleton.data.sample(n=1)

        if random_row is None:
            raise HTTPException(status_code=500, detail='CSV file not loaded')

        ip = random_row.iloc[0]['srcip']
        port = random_row.iloc[0]['sport'].astype(str)
        input_id = random_row.iloc[0]['index']

        index = int(random_row.iloc[0]['category_label'])
        label = self.label_util.get_category_label()[index]

        if label in self.label_util.get_user_label():
            user = self.dummy_user_repository.find_by_attack_type(label)
            body = {
                'username': user.username,
                'password': user.password
            }
        elif label in self.label_util.get_script_label():
            if label in self.label_util.get_restricted_script_label():
                script = self.dummy_script_repository.find_random()
                body = {
                    'script': script.content
                }
            else:
                script = self.dummy_script_repository.find_random_by_attack_type(label)
                body = {
                    'script': script.content
                }
        else:
            body = {}

        body['timestamp'] = str(datetime.datetime.now())

        request_data = {
            'ip': ip,
            'port': port,
            'input_id': input_id,
            'body': body,
            'packet_info': self.packet_info_schema.from_dataframe(random_row.iloc[0])
        }

        # self.logger.info(f'attack type is {label}')
        # self.logger.info(f'packet data = {request_data}')

        try:
            response = requests.post(self.url, json=request_data)
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Error sending POST request: {str(e)}')
