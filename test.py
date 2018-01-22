from unittest import TestCase
from MP0 import listify, delimiters

sample_in = """Billy_Reeves
Smorz
Nationalist_Left_-_Youth
Ancient_Greek_units_of_measurement
Jiuting_(Shanghai_Metro)"""

class TestListify(TestCase):

    def test_listify(self):
        self.assertEqual(listify(sample_in),
                         ["Billy", "Reeves", "Smorz", "Nationalist", "Left", "Youth",
                         "Ancient", "Greek", "units", "of", "measurement", "Jiuting", "Shanghai", "Metro"])
