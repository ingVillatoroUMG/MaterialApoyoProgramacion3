class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def retirar_primero(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def retirar_ultimo(self):
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = None

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

mi_lista = ListaSimple()
mi_lista.agregar_elemento("Juan")
mi_lista.agregar_elemento("Maria")
mi_lista.agregar_elemento("Jose")
mi_lista.agregar_elemento("Douglas")
mi_lista.agregar_elemento("Pedro")
print("Muestra la lista inicialmente completa")
mi_lista.imprimir_lista()
print("Retira el ultimo elemento de la lista")
mi_lista.retirar_ultimo()
mi_lista.imprimir_lista()
print("Retira el primer elemento de la lista")
mi_lista.retirar_primero()
mi_lista.imprimir_lista()