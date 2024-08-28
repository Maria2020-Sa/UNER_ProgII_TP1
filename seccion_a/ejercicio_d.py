def listas_diferencia(lista1, lista2):
    comunes = list(set(lista1) & set(lista2))
    comunes.sort(reverse=True)
    
    no_comunes = list(set(lista1).symmetric_difference(set(lista2)))
    no_comunes.sort()
    
    print(comunes)
    print(no_comunes)

listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
