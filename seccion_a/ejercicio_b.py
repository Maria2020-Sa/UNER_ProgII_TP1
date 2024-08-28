def es_abc(palabra):
    return list(palabra) == sorted(palabra)


print(es_abc("abcde"))