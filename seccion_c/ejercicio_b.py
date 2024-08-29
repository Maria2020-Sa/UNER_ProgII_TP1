'''Escribir un programa que resuelva la secuencia de Fibonacci a pedido del
usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro
numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio
anterior, validado. La función debe encargarse de calcular la secuencia para
dicho número'''

def fibonacci(numero):
    if numero < 0:
        return "El número debe ser un entero no negativo."
    
    # Casos base
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    
    # Inicializar los primeros dos valores de la secuencia
    a, b = 0, 1
    
    # Calcular la secuencia hasta el número pedido
    for _ in range(2, numero + 1):
        a, b = b, a + b
    
    return b

def validar_entrada():
    while True:
        entrada = input("Ingresa un número entero no negativo: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Entrada inválida. Por favor, ingresa un número entero no negativo.")

# Ejemplo de uso
numero = validar_entrada()
resultado = fibonacci(numero)
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")
