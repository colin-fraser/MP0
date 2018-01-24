from unittest import TestCase
from MP0 import listify, delimiters, handle_tokens

sample_in = """Billy_Reeves
Smorz
Nationalist_Left_-_Youth
Ancient_Greek_units_of_measurement
Jiuting_(Shanghai_Metro),
ab
ab
ab
ac
ac
ac
aa
"""

class TestListify(TestCase):
    def test_listify(self):
        self.assertEqual(listify(sample_in),
                         ["billy", "reeves", "smorz", "nationalist", "left", "youth",
                          "ancient", "greek", "units", "of", "measurement", "jiuting", "shanghai", "metro",
                          "ab", "ab", "ab", "ac", "ac", "ac", "aa"])
        # self.assertEqual(listify('a a\ta,a;a.a?a!a-a:a@a[a]a(a)a{a}a_a*a/a'),
        #                           ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a'])


class TestHandle_tokens(TestCase):
    def test_handle_tokens(self):
        tokens = listify(sample_in)
        h = handle_tokens(tokens)
        print(h)
