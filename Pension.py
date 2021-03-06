from datetime import datetime
from datetime import date
from datetime import timedelta

def verification (age, sex, situation, SDate):
    # Fecha actual
    actual = date.today()

    # Semanas reglamentarias
    diasCotizados = 750*7

    # Edad reglamentaria
    edadH = 60
    edadM = 55

    paid = (actual - SDate).days
    if (paid >= diasCotizados):
        if(sex == 1): # Los masculinos
            if(situation == 0 and age >= edadH): # Situacion salubre y dentro del rango debido
                return True
            elif(situation == 1): # Situacion insalubre
                Fnumber = (paid/365) // 4 # Numero de anios en los que trabaja insalubre
                if(Fnumber >= 1 and Fnumber <= 5): # El numero de anios permitido
                    return age >= edadH - Fnumber
                elif(Fnumber > 5):
                    return age >= edadH -5
            elif(situation == 0 and age < edadH): # Situacion salubre y fuera del rango debido
                return False

        elif(sex == 0): # Las masculinas
            if(situation == 0 and age >= edadM): # Situacion salubre y dentro del rango debido
                return True
            elif(situation == 1): # Situacion insalubre
                Fnumber = (paid/365) // 4 # Numero de anios en los que trabaja insalubre
                if(Fnumber >= 1 and Fnumber <= 5): # El numero de anios permitido
                    return age >= edadM - Fnumber
                elif (Fnumber > 5):
                    return age >= edadM - 5
            elif(situation == 0 and age < edadM): # Situacion salubre y fuera del rango debido
                return False
    else:
        return False


if __name__ == '__main__':

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
