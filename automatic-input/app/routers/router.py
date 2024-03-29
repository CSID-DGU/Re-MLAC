from fastapi import APIRouter
from app.handlers.packet_handler import PacketHandler
from app.handlers.predict_handler import PredictHandler
from app.handlers.test_handler import TestHandler
from app.schemas.test_schema import RequestSchema

router = APIRouter()
packet_handler = PacketHandler()
predict_handler = PredictHandler()
test_handler = TestHandler()


@router.get("/")
def automatic_input_router():
    return packet_handler.handle_request()


@router.get("/predict")
def predict_label_router():
    return predict_handler.predict_reqeust()


@router.post("/test")
def test_input_router(request: RequestSchema):
    return test_handler.test_request(request)
