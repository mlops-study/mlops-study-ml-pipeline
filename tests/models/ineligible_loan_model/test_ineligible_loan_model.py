import os
from unittest import TestCase
from airflow.models import Variable
from support.date_values import DateValues
from tests import context

home_dir = os.path.expanduser("~")
airflow_dags_path = Variable.get("AIRFLOW_DAGS_PATH")
os.environ['MLOPS_DATA_STORE'] = f"{home_dir}/airflow/mlops_data_store"
os.environ['MODEL_OUTPUT_HOME'] = f"{airflow_dags_path}/models/ineligible_loan_model"
os.environ['FEATURE_STORE_URL'] = f"mysql+pymysql://root:root@localhost/mlops"


class TestIneligibleLoanModel(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        from support.infra.mysql import Mysql
        cls.mysql = Mysql()
        # Common Given
        cls.base_day = DateValues().get_before_one_day()
        cls.context = context

    def setUp(self) -> None:
        pass

    def test_data_extract(self):
        import models.ineligible_loan_model.ineligible_loan_model as model

        # When
        model.data_extract.__setattr__('sql', model.queries.replace('{{ yesterday_ds_nodash }}', self.base_day))
        model.data_extract.execute(self.context)

        # Then
        sql = \
            f"""
            select count(1) as cnt
              from mlops.ineligible_loan_model_features
             where base_dt = '{self.base_day}'
            """
        actual = self.mysql.read_sql(sql=sql)
        self.assertTrue(actual["cnt"][0])

    def test_data_preparation(self):
        import models.ineligible_loan_model.ineligible_loan_model as model
        from models.ineligible_loan_model.data_preparation.preparation import Preparation

        # When
        preparation = Preparation(model_name=model.model_name, model_version=model.model_version,
                                  base_day=self.base_day)
        preparation.preprocessing()

    def test_data_preparation_of_dag_task(self):
        import models.ineligible_loan_model.ineligible_loan_model as model
        context = {}
        env = {"PYTHON_FILE": "/home/mlops/data_preparation/preparation.py",
               "MODEL_NAME": model.model_name,
               "MODEL_VERSION": model.model_version,
               "BASE_DAY": self.base_day}
        model.data_preparation.__setattr__("env", env)
        model.data_preparation.execute(context)

    def test_prediction(self):
        import models.ineligible_loan_model.ineligible_loan_model as model
        from models.ineligible_loan_model.model.prediction import Prediction

        # When
        prediction = Prediction(model_name=model.model_name, model_version=model.model_version,
                                base_day=self.base_day)
        prediction.predict()

    def test_prediction_of_dag_task(self):
        import models.ineligible_loan_model.ineligible_loan_model as model
        context = {}
        env = {"PYTHON_FILE": "/home/mlops/model/prediction.py",
               "MODEL_NAME": model.model_name,
               "MODEL_VERSION": model.model_version,
               "BASE_DAY": self.base_day}
        model.prediction.__setattr__("env", env)
        model.prediction.execute(context)

    @classmethod
    def tearDownClass(cls) -> None:
        print("Dose not stop the impala_docker!")
