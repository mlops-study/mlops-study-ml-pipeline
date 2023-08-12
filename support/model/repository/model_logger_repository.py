import json
from typing import Union, Dict
from support.infra.mysql import Mysql


class ModelLoggerRepository:
    def __init__(self,
                 model_name: str,
                 model_version: str,
                 db: Mysql = Mysql()):
        self._model_name = model_name
        self._model_version = model_version
        self._db = db

    def logging_init(self):
        sql = f"""
            delete
              from mlops.model_ct_log
             where model_name = '{self._model_name}'
               and model_version = '{self._model_version}'
            """
        self._db.execute(sql=sql)

    def logging_started(self):
        sql = f"""
            insert into mlops.model_ct_log (model_name, model_version)
            values ('{self._model_name}', '{self._model_version}');
            """
        self._db.execute(sql=sql)

    def logging_finished(self, metrix: str):
        sql = f"""
            update mlops.model_ct_log
               set metrix = '{metrix}'
             where model_name = '{self._model_name}'
               and model_version = '{self._model_version}'
            """
        self._db.execute(sql=sql)
