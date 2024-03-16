from fastapi import APIRouter
from app.schemas.schema import PostDataRequest
from app.handlers.handler import post_data

router = APIRouter()


@router.get("/")
def post_data_route():
    return post_data()


@router.post("/")
def test_post_data_route(request: PostDataRequest):
    return post_data()