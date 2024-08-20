'''Escribir una función de nombre palabra_no_tiene_letras(palabra,
letras_prohibidas), la cual retorne True si es que los caracteres que componen
una palabra no se encuentran en una lista de caracteres prohibidos.'''

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    letras_encontradas = []

    for letra in palabra:
        if letra in letras_prohibidas:
            letras_encontradas.append(letra)

    if letras_encontradas: #Si la lista no esta vacía.
        print(f"La palabra {palabra} contiene las letras prohibidas: {', '.join(letras_encontradas)}")
        return False
    else:
        print(f"La palabra {palabra}, no contiene letras prohibidas.")
        return True

palabra = input("Ingrese una palabra:\n ")
letras_prohibidas = input("ingrese las letras prohibidas separadas por coma:\n ").split(', ')
palabra_no_tiene_letras(palabra, letras_prohibidas)
