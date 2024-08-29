import time
from funciones import validar_edad, anio_bisiesto, calcular_dias_mes
    
# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = validar_edad(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = 0

def calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0

    # Calcular los días completos en los años entre anio_comienzo y anio_fin
    for a in range(anio_comienzo, anio_fin):
        if anio_bisiesto(a):
            dias += 366
        else:
            dias += 365

    # Agregar los días transcurridos en el año actual
    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
    
    # Agregar los días del mes actual
    dias += hora_local.tm_mday

    return dias

# agregar los días transcurridos en este mes
dias = dias + hora_local.tm_mday

# imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))