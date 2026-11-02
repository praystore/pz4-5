from django.test import TestCase
from .models import (
    DataGeneratorFactory,
    UsersDataGenerator,
    OrdersDataGenerator,
    ProductsDataGenerator,
)
class FactoryTest(TestCase):
    def test_creates_correct_types(self):
        self.assertIsInstance(DataGeneratorFactory.create("users", 2), UsersDataGenerator)
        self.assertIsInstance(DataGeneratorFactory.create("orders", 2), OrdersDataGenerator)
        self.assertIsInstance(DataGeneratorFactory.create("products", 2), ProductsDataGenerator)
    def test_generation(self):
        gen = DataGeneratorFactory.create("users", 3)
        self.assertEqual(len(gen.generate()), 3)
    def test_unknown_type_raises(self):
        with self.assertRaises(ValueError):
            DataGeneratorFactory.create("unknown", 1)