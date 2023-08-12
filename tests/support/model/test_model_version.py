from unittest import TestCase


class TestModelVersion(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        from support.model.model_version import ModelVersion
        model_name = "ineligible_loan_model"
        cls.model_version = ModelVersion(model_name=model_name)

    def test_get_ct_model_version(self):
        ct_model_version = self.model_version.get_ct_model_version()
        print(f"ct_model_version = {ct_model_version}")
