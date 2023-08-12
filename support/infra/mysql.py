import os
from sqlalchemy import create_engine, text
from pandas import DataFrame
from pandas.io.sql import read_sql, execute

feature_store_url = os.getenv('FEATURE_STORE_URL', "")


class Mysql:
    def __init__(self,
                 url: str = feature_store_url):
        self._engine = create_engine(url)

    def read_sql(self, sql: str) -> DataFrame:
        with self._engine.connect() as conn:
            return read_sql(text(sql), con=conn)

    def execute(self, sql: str, params=None):
        with self._engine.connect() as conn:
            return execute(text(sql), con=conn, params=params)
