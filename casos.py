import unittest
import Pension

from datetime import date


class PensionStatus(unittest.TestCase):

    # Mujer trabajando en lugares salubres y cumple las 750 semanas. Optiene a pension 
    def test_female_healthy(self):
        edad = 55
        sexo = 0
        situation = 0 
        self.assertTrue(Pension.verification(edad, sexo, situation, date(1993,2,13)), 'No se cumplen los requisitos')

    #  Mujer trabajando en lugares salubres y no las 750 semanas. No optiene a pension 
    def test_female_healthy_not(self):
        edad = 60
        sexo = 0
        situation = 0 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2010,2,13)), 'No se cumplen los requisitos')

    #  Mujer menor a 55, trabajando en lugares salubres y cumple 750 semanas. No optiene a pension 
    def test_female_healthy_not_age(self):
        edad = 50
        sexo = 0
        situation = 0 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2000,2,13)), 'No se cumplen los requisitos')

    #########################################################
    ######## Mujer no trajando en lugares insalubres ########

    # Mujer trabajando en lugares insalubres 
    def test_female_unHealthy(self):
        edad = 50
        sexo = 0
        situation = 1 
        self.assertTrue(Pension.verification(edad, sexo, situation, date(1993,2,13)), 'No se cumplen los requisitos')

    # Mujer trabajando en lugares no salubres, cumple con la edad y no las 750 semanas. No optiene a pension 
    def test_female_unhealthy_not(self):
        edad = 55
        sexo = 0
        situation = 1 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2010,2,13)), 'No se cumplen los requisitos')

    # Mujer trabajando en lugares no salubres, no cumple con la edad y cumple las 750 semanas. No optiene a pension 
    def test_female_unhealthy_not_age(self):
        edad = 51
        sexo = 0
        situation = 1 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2004,2,13)), 'No se cumplen los requisitos')

    ########################################################
    ######### Hombre trabajando en lugares saludres ########

    # Hombre trabajando en lugares salubre, cumple con la edad y las 750 semanas
    def test_male_healthy(self):
        edad = 60
        sexo = 1
        situation = 0 
        self.assertTrue(Pension.verification(edad, sexo, situation, date(2000,2,13)), 'No se cumplen los requisitos')

    # Hombre trabajando en lugares salubre, cumple con la edad y no las 750 semanas
    def test_male_healthy_not(self):
        edad = 65
        sexo = 1
        situation = 0 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2013,2,13)), 'No se cumplen los requisitos')

    # Hombre trabajando en lugares salubre, no cumple con la edad y las 750 semanas
    def test_male_healthy_not_ages(self):
        edad = 55
        sexo = 1
        situation = 0 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(1993,2,13)), 'No se cumplen los requisitos')

    ##########################################################
    ######### Hombre trabajando en lugares insaludres ########

    # Hombre trabajando en lugares insalubres, cumple con la edad y las 750 semanas
    def test_male_unhealthy(self):
        edad = 56
        sexo = 1
        situation = 1 
        self.assertTrue(Pension.verification(edad, sexo, situation, date(2000,2,13)), 'No se cumplen los requisitos')

    # Hombre trabajando en lugares insalubres, cumple con la edad y no las 750 semanas
    def test_male_unhealthy_not(self):
        edad = 65
        sexo = 1
        situation = 1 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2012,2,13)), 'No se cumplen los requisitos')

    # Hombre trabajando en lugares insalubres, no cumple con la edad y las 750 semanas
    def test_male_unhealthy_not_ages(self):
        edad = 55
        sexo = 1
        situation = 1 
        self.assertFalse(Pension.verification(edad, sexo, situation, date(2005,2,13)), 'No se cumplen los requisitos')

   
if __name__ == '__main__':
    unittest.main()