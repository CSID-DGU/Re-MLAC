from datetime import datetime
from app.configs.data import TestDataSingleton, DataFrameSingleton

from fastapi import HTTPException
import requests

from app.schemas.test_schema import TestSchema
from app.utils.label_util import LabelUtil


class PredictHandler:
    def __init__(self):
        self.test_data = TestDataSingleton()
        self.dataframe = DataFrameSingleton()
        self.label_util = LabelUtil()
        self.packet_info_schema = TestSchema()

    def predict_reqeust(self):

        dataframe = self.dataframe.data
        length = self.dataframe.length

        for index in range(length):
            row = dataframe.iloc[index]

            print(index)
            ip = row['srcip']
            port = row['sport'].astype(str)
            index = int(row['category_label'])
            label = self.label_util.get_category_label()[index]
            timestamp = str(datetime.now())

            request_data = {
                'ip': ip,
                'port': port,
                'timestamp': timestamp,
                'body': [],
                'packet_info': self.packet_info_schema.from_dataframe(row)
            }
            try:
                response = requests.get('http://210.94.179.19:9253/packets/analysis', json=request_data)
                attack_type = response.json().get('attack_type')
                self.test_data.save(label, attack_type)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        self.test_data.save_to_csv('data/result/web_attack_xss_predict.csv')
