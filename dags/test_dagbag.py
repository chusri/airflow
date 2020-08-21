import unittest
from airflow.models import DagBag

def test_dags_load_with_no_errors():
    dag_bag = DagBag(include_examples=False)
    dag_bag.process_file('Lendkey-DagTemplate-Simple-V1.py')
    assert len(dag_bag.import_errors) == 0

if __name__ == '__main__':
    unittest.main()
