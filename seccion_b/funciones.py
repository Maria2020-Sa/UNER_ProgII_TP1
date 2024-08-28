from calendar import isleap

# a. Se elimine la sentencia if / else de la función anio_bisiesto.
def anio_bisiesto(anio):
    #if isleap(anio): return True
    #else: return False
    return isleap(anio)

# b. Las múltiples sentencias if la función dia_mes utilicen la cláusula in en lugar de varias cláusulas or
def calcular_dias_mes(mes, anio_bisiesto):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2 and anio_bisiesto == True:
        return 29
    elif mes == 2 and anio_bisiesto == False:
        return 28
    
#c. Se agregue una sentencia que valide que la edad ingresada por el usuario es numérica.
def validar_edad (edad):
    try:
        edad = int(edad)
        if edad < 0:
            print("La edad no puede ser un valor negativo.")
            return False
        else:
            return edad
    except ValueError:
        print("Error: La edad debe ser un número.")
        return False