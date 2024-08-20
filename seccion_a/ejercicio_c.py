'''Escriba un procedimiento procesar_palabras(entrada) que acepte una
secuencia de palabras separadas por coma, las ordene y las imprima.
Suponiendo que la entrada provista al programa es la siguiente:
te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te'''

def procesar_palabras(entrada):
    lista_entrada = [item.strip() for item in entrada.split(',')]
    lista_entrada.sort()
    print(", ".join(lista_entrada))

palabras = input("Ingrese secuencia de palabras separadas por coma:\n ")
procesar_palabras(palabras)