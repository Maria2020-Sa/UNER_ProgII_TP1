'''c. Tal como sucede con la lógica proposicional, en Python muchas veces las
expresiones booleanas pueden ser simplificadas manteniendo el valor de
verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente
a a and b. A continuación, intente simplificar las siguientes expresiones y
escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el
valor de verdad de las expresiones ya simplificadas:
i. (a or b) or (b and c)
ii. b and c or False
iii. a and b or c or (b and a)
iv. a == True or b == False'''

def procesar_sentencias(a, b, c):
    resultado_1 = a or b or c  # Simplificación de (a or b) or (b and c)
    resultado_2 = b and c      # Simplificación de b and c or False
    resultado_3 = a and b or c # Simplificación de a and b or c or (b and a)
    resultado_4 = a or not b   # Simplificación de a == True or b == False
    
    return resultado_1, resultado_2, resultado_3, resultado_4

# Ejemplo de uso
a = True
b = False
c = True
print(procesar_sentencias(a, b, c))
