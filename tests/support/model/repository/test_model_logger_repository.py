from unittest import TestCase


class TestModelLoggerRepository(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        model_name = 'ineligible_loan_model'
        model_version = "1.0.1"
        from support.model.repository.model_logger_repository import ModelLoggerRepository
        cls.model_logger_repository = ModelLoggerRepository(model_name=model_name, model_version=model_version)

    def test_logging_init_and_started(self):
        self.model_logger_repository.logging_init()
        self.model_logger_repository.logging_started()

    def test_logging_finished(self):
        metrix = {"accuracy": 87.12313}
        self.model_logger_repository.logging_finished(metrix=metrix)
