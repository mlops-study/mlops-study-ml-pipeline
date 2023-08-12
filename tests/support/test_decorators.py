from unittest import TestCase


class TestDecorators(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def setUp(self) -> None:
        pass

    def test_elapsed_time(self):
        from support.decorators import elapsed_time
        @elapsed_time
        def test_func():
            print("test_func has finished!")
            return True

        self.assertTrue(test_func())
