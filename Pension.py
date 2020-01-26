from datetime import datetime
from datetime import date
from datetime import timedelta

def verification (age, sex, situation, SDate):
    paid = (actual - SDate).days
    if (paid >= 750*5):
        if(sex == 1): # Los masculinos
            if(situation == 0 and age >= 60): # Situacion salubre y dentro del rango debido
                return True
            elif(situation == 1): # Situacion insalubre
                Fnumber = (paid/365) // 4 # Numero de anios en los que trabaja insalubre
                if(Fnumber >= 1 and Fnumber <= 5): # El numero de anios permitido
                    if(age >= 60 - Fnumber):
                        return True
                    else:
                        return False
            elif(situation == 0 and age < 60): # Situacion salubre y fuera del rango debido
                return False

        elif(sex == 0): # Las masculinas
            if(situation == 0 and age >= 55): # Situacion salubre y dentro del rango debido
                return True
            elif(situation == 1): # Situacion insalubre
                Fnumber = (paid/365) // 4 # Numero de anios en los que trabaja insalubre
                if(Fnumber >= 1 and Fnumber <= 5): # El numero de anios permitido
                    if(age >= 55 - Fnumber):
                        return True
                    else:
                        return False
            elif(situation == 0 and age < 55): # Situacion salubre y fuera del rango debido
                return False
    else:
        return False




# Fecha actual
actual = date.today()

# Datos par la fecha de inicio de trabajo
year = int(input("Anyo de 4 cifras: "))
month = int(input("Mes: "))
day = int(input("Dia: "))
SDate = date(year, month, day)

# Datos para la verificacion de pension
age = int(input("Age: "))
sex = int(input("Sexo(1 = Masculino, 0 = Femenino): "))
situation = int(input("¿Considera que trabaja bajo condiciones salubres(1) o insalubres(0)?: "))
verification(age, sex, situation, SDate)
