from django.test import TestCase
from orden.models import *

class TestModel(TestCase):
    def test_prueba_humo(self):
        self.assertEqual(2+2, 4)

    def test_agrega_proveedor(self):
        pass