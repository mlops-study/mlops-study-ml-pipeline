from unittest import TestCase


class TestModelLogger(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        from support.model.model_logger import ModelLogger
        model_name = "ineligible_loan_model"
        model_version = "1.0.1"
        cls.model_logger = ModelLogger(model_name=model_name, model_version=model_version)

    def test_01_logging_started(self):
        self.model_logger.logging_started()

    def test_02_logging_finished(self):
        metrix = {"accuracy": 90.23211}
        self.model_logger.logging_finished(metrix=metrix)
