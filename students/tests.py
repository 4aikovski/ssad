from django.test import TestCase
from students.models import student


class TestStudent(TestCase):
    def test_short_str(self):
        s = student()
        s.last_name = "Сидоров"
        s.First_name = "Сидор"
        s.numver = '1244'
        res = str(s)
        self.assertEqual(res,"Сидоров С")
# Create your tests here.

    def test_long_str(self):
        s = student()
        s.last_name = "Сидоров"
        s.First_name = "Сидор"
        s.Second_name = "Сидорович"
        s.numver = '1244'
        res = str(s)
        self.assertEqual(res,"Сидоров СС")
# Create your tests here.
