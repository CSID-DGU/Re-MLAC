import os
import uvicorn
from fastapi import FastAPI
from app.routers.router import router
from app.handlers.handler import initialize_dataframe
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

initialize_dataframe(os.getenv("DATA_PATH"), os.getenv("BODY_PATH"))
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
