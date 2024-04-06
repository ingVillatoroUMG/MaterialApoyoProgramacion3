import math

def altura_arbol(n):
    return math.log2(n + 1)

# Ejemplo
nodos = 9
altura = altura_arbol(nodos)
print("Altura del árbol con", nodos, "nodos:", altura)
