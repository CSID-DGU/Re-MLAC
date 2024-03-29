import pandas as pd
from fastapi import HTTPException


class PandasUtil:
    @staticmethod
    def read_csv_file(file_path: str) -> pd.DataFrame:
        try:
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail=f'File not found: {file_path}: from {str(e)}')
