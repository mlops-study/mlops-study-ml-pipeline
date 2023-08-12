import json
from typing import Union, Dict
from support.model.repository.model_logger_repository import ModelLoggerRepository


class ModelLogger:
    def __init__(self,
                 model_name: str,
                 model_version: str):
        self._model_name = model_name
        self._model_version = model_version
        self._model_logger_repository = ModelLoggerRepository(model_name=model_name, model_version=model_version)

    def logging_started(self):
        self._model_logger_repository.logging_init()
        self._model_logger_repository.logging_started()

    def logging_finished(self, metrix: Union[str, Dict]):
        if isinstance(metrix, dict):
            metrix = json.dumps(metrix)
        self._model_logger_repository.logging_finished(metrix=metrix)
