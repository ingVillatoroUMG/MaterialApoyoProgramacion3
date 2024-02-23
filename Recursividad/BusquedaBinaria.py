def busqueda_binaria_recursiva(lista, elemento, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            return busqueda_binaria_recursiva(lista, elemento, medio + 1, fin)
        else:
            return busqueda_binaria_recursiva(lista, elemento, inicio, medio - 1)
    else:
        return -1


lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_a_buscar = 7

resultado = busqueda_binaria_recursiva(lista_ordenada, elemento_a_buscar)

print(resultado)
