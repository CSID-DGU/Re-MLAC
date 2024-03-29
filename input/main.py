import os
import uvicorn
from fastapi import FastAPI

from app.routers.router import router
from app.configs.data import DataFrameSingleton
from app.utils.pandas_util import PandasUtil
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
dataframe = DataFrameSingleton()
pandas_util = PandasUtil()

dataframe.data = pandas_util.read_csv_file(os.getenv('DATA_PATH'))
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
