'''Escribir una función suma(numero) que resuelva la siguiente suma, 
asumiendo que numero = 10:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
En el programa que invoque dicha función:
i. El usuario debe poder ingresar el valor del parámetro numero.
ii. Debe validarse que el dato ingresado por el usuario corresponda a
un dígito, y no a otro tipo de dato como un carácter.
iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for,
while).
BONUS: Luego, codificar una función equivalente que utilice recursividad.'''

def validar_numero (numero):
    try:
        numero = int(numero)
        if numero > 0 or numero < 0:
            return numero
    except ValueError as e:
        print("Error: El valor debe ser un número.")
        return False

def suma (numero):
    numero = validar_numero(numero)
    contador = 0
    for digito in range(1, numero+1):
        contador += digito
    return contador

def suma_recursiva(numero):
    numero = validar_numero(numero)
    # Caso base: 
    if numero == 1:
        return 1
    else:
        # Caso recursivo:
        return numero + suma_recursiva(numero-1)
    
def mostrar_suma_digitos (numero):
    print("Sin Recursividad: ")
    print(f"La suma de los dígitos del número {numero} es: {suma(numero)}")
    try:
        print("Con Recursividad: ")
        print(f"La suma de los dígitos del número {numero} es: {suma_recursiva(numero)}")
    except Exception as e:
        print("Error: supero el número 998")
        return 0

numero_usuario = input("Ingrese un valor: ")
mostrar_suma_digitos(numero_usuario)