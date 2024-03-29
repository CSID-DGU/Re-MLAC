from fastapi import HTTPException

from app.schemas.test_schema import RequestSchema
from dotenv import load_dotenv
import requests
import os

load_dotenv()


class TestHandler:
    def __init__(self):
        self.request_schema: RequestSchema = RequestSchema()
        self.url = os.getenv('POST_URL')

    def test_request(self, request_schema: RequestSchema):
        print(self.url)
        try:
            response = requests.post(self.url, json=request_schema.dict())
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Error sending POST request: {str(e)}')