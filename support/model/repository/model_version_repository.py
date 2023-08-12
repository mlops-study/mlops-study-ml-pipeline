import json
from typing import Union, Dict
from support.infra.mysql import Mysql


class ModelVersionRepository:
    def __init__(self,
                 db: Mysql = Mysql()):
        self._db = db

    def get_current_model_version(self, model_name: str) -> str:
        sql = f"""
            select max(model_version) as max_model_version
              from mlops.model_ct_log
             where model_name = '{model_name}'
            """
        max_model_version = self._db.execute(sql=sql).fetchone()[0]
        return max_model_version
