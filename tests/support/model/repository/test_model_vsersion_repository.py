from unittest import TestCase


class TestModelVersionRepository(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        from support.model.repository.model_version_repository import ModelVersionRepository
        cls.model_version_repository = ModelVersionRepository()

    def test_get_current_model_version(self):
        model_name = 'ineligible_loan_model'
        current_model_version = self.model_version_repository.get_current_model_version(model_name=model_name)
        print(f"current_model_version = {current_model_version}")
