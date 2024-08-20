'''Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de
números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista
e imprima ambas. La lista de números la ingresa el usuario en forma de números
separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81'''

def numeros_par_impar(numeros):
    lista_numeros = numeros.split(",")
    lista_numeros = [int(num.strip()) for num in lista_numeros]
    lista_impar = [impar for impar in lista_numeros if impar % 2 != 0]
    lista_par = [par for par in lista_numeros if par % 2 == 0]
    impar_cuadrados = []

    for cuadrado in lista_impar:
        cuadrado *= cuadrado
        impar_cuadrados.append(cuadrado)
    print(f"""
 Lista Par: {lista_par}
 Lista Impar al cuadrado: {impar_cuadrados}""")
    

numeros = input("Ingrese números separados por coma:\n ")
numeros_par_impar(numeros)