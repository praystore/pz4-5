from django.test import TestCase
from .singleton import TestDataManager
class SingletonTest(TestCase):
    def test_single_instance(self):
        m1 = TestDataManager()
        m2 = TestDataManager()
        self.assertIs(m1, m2)
        self.assertEqual(id(m1), id(m2))
    def test_shared_state(self):
        m1 = TestDataManager()
        m1.clear()
        m1.add_dataset("users", ["a", "b"])
        m2 = TestDataManager()
        self.assertEqual(m2.get_dataset("users"), ["a", "b"])