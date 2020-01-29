import unittest
import Pension

from datetime import date


class PensionStatus(unittest.TestCase):

    # Mujer trabajando en lugares salubres. Optiene a pension
    def test_female_healthy(self):
        edad = 55
        sexo = 0
        situation = 0 
        self.assertTrue(Pension.verification(edad, sexo, situation, date(1993,2,13)), 'No se cumplen los requisitos')

    def test_female_healthy_not(self):
        edad = 60
        sexo = 0
        situation = 0 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2010,2,13)), 'No se cumplen los requisitos')

    # # Mujer trabajando en lugares insalubres 
    def test_female_notHealthy(self):
        edad = 50
        sexo = 0
        situation = 1 
        self.assertTrue(Pension.verification(edad, sexo, situation, date(1993,2,13)), 'No se cumplen los requisitos')


    # # Hombre trabajando en lugares salubrelols
    def test_male_healthy(self):
        edad = 55
        sexo = 0
        situation = 1 
        self.assertTrue(Pension.verification(edad, sexo, situation, date(1993,2,13)), 'No se cumplen los requisitos')

    # # Hombre trabajando en lugares insalubres
    # def test_male_notHealthy(self):
    #     startwork = date(year, month, day)
    #     age = date(year, month, day)
    #     self.assertTrue(Pension.verification , 1, 1)
        
    # # Cumple con los requisitos legales para recibir una pensión de vejez
    # def test_approve(self):
    #     self.assertTrue(Pension.verification , True)

    # # No cumple con los requisitos legales para recibir una pensión de vejez
    # def test_disapprove(self):
    #     self.assertTrue(Pension.verification , True)
if __name__ == '__main__':
    unittest.main()