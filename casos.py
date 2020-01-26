import unittest
import pension

class PensionStatus(unittest.TestCase):

    # Mujer trabajando en lugares salubres
    def test_female_healthy(self):
        startwork = date(year, month, day)
        age = date(year, month, day)
        self.assertTrue(pension. , 0, 0)

    # Mujer trabajando en lugares insalubres
    def test_female_notHealthy(self):
        startwork = date(year, month, day)
        age = date(year, month, day)
        self.assertTrue(pension. , 0, 1)

    # Hombre trabajando en lugares salubres
    def test_male_healthy(self):
        startwork = date(year, month, day)
        age = date(year, month, day)
        self.assertTrue(pension. , 1, 0)

    # Hombre trabajando en lugares insalubres
    def test_male_notHealthy(self):
        startwork = date(year, month, day)
        age = date(year, month, day)
        self.assertTrue(pension. , 1, 1)
        
    # Cumple con los requisitos legales para recibir una pensión de vejez
    def test_approve(self):
        self.assertTrue(pension. , True)

    # No cumple con los requisitos legales para recibir una pensión de vejez
    def test_disapprove(self):
        self.assertTrue(pension. , True)
