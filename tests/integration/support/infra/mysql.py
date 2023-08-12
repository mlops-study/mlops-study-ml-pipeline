from unittest import TestCase


class TestMysql(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def setUp(self) -> None:
        pass

    def test_new_data_values(self):
        from support.infra.mysql import Mysql
        mysql = Mysql()
        sql = """select 1"""
        actual = mysql.read_sql(sql=sql)
        print(actual)




