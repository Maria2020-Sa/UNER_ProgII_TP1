from calendar import isleap

# a. Se elimine la sentencia if / else de la función anio_bisiesto.
def anio_bisiesto(anio):
    #if isleap(anio): return True
    #else: return False
    return isleap(anio)

# b. Las múltiples sentencias if la función dia_mes utilicen la cláusula in en lugar de varias cláusulas or
def calcular_dias_mes(mes, anio_bisiesto):
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif mes in {4, 6, 9, 11}:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28
    
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