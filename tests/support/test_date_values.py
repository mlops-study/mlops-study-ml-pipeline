from unittest import TestCase


class TestDateValues(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def setUp(self) -> None:
        pass

    def test_get_before_one_day(self):
        from support.date_values import DateValues
        print(DateValues.get_before_one_day())
