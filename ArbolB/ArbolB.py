import graphviz

class NodoArbolB:
    def __init__(self, hoja=False, t=None):
        self.hoja = hoja
        self.claves = []
        self.hijos = []
        self.t = t

    def esta_lleno(self):
        return len(self.claves) == (2 * self.t) - 1

    def es_menor_minimo(self):
        return len(self.claves) < self.t - 1

# Árbol B
class ArbolB:
    def __init__(self, t):
        self.raiz = NodoArbolB(hoja=True, t=t)
        self.t = t

    # Insertar nodo
    def insertar(self, clave):
        if self.raiz.esta_lleno():
            temp = NodoArbolB(t=self.t)
            temp.hijos.insert(0, self.raiz)
            self.dividir_hijo(temp, 0)
            self.raiz = temp
        self.insertar_no_lleno(self.raiz, clave)

    # Insertar en no lleno
    def insertar_no_lleno(self, x, clave):
        i = len(x.claves) - 1
        if x.hoja:
            x.claves.append((None, None))
            while i >= 0 and clave[0] < x.claves[i][0]:
                x.claves[i + 1] = x.claves[i]
                i -= 1
            x.claves[i + 1] = clave
        else:
            while i >= 0 and clave[0] < x.claves[i][0]:
                i -= 1
            i += 1
            if x.hijos[i].esta_lleno():
                self.dividir_hijo(x, i)
                if clave[0] > x.claves[i][0]:
                    i += 1
            self.insertar_no_lleno(x.hijos[i], clave)

    # Dividir el hijo
    def dividir_hijo(self, x, i):
        y = x.hijos[i]
        z = NodoArbolB(hoja=y.hoja, t=self.t)
        x.hijos.insert(i + 1, z)
        x.claves.insert(i, y.claves[self.t - 1])
        z.claves = y.claves[self.t: (2 * self.t) - 1]
        y.claves = y.claves[0: self.t - 1]
        if not y.hoja:
            z.hijos = y.hijos[self.t: 2 * self.t]
            y.hijos = y.hijos[0: self.t - 1]

    # Imprimir el árbol
    def imprimir_arbol(self, x, l=0):
        print("Nivel ", l, " ", len(x.claves), end=":")
        for i in x.claves:
            print(i, end=" ")
        print()
        l += 1
        if len(x.hijos) > 0:
            for i in x.hijos:
                self.imprimir_arbol(i, l)

    # Buscar clave en el árbol
    def buscar_clave(self, clave, x=None):
        if x is not None:
            i = 0
            while i < len(x.claves) and clave > x.claves[i][0]:
                i += 1
            if i < len(x.claves) and clave == x.claves[i][0]:
                return (x, i)
            elif x.hoja:
                return None
            else:
                return self.buscar_clave(clave, x.hijos[i])
        else:
            return self.buscar_clave(clave, self.raiz)

    # Generar representación Graphviz del árbol
    def generar_graphviz(self, filename='arbolb.png'):
        def agregar_nodo(nodo, num_nodo, num_padre=None):
            nonlocal contador_nodos
            if nodo is not None:
                etiqueta_nodo = '| '.join([f"{clave[1]}" for clave in nodo.claves])
                g.node(f"{num_nodo}", label=etiqueta_nodo, shape='record')
                if num_padre is not None:
                    g.edge(f"{num_padre}", f"{num_nodo}")
                for i, hijo in enumerate(nodo.hijos):
                    contador_nodos += 1
                    agregar_nodo(hijo, contador_nodos, num_nodo)

        g = graphviz.Digraph('arbolb', format='png', filename=filename)
        contador_nodos = 0
        agregar_nodo(self.raiz, contador_nodos)
        g.render(view=False)

def main():
    B = ArbolB(5)

    for i in range(100):
        B.insertar((i, 2 * i))

    B.imprimir_arbol(B.raiz)

    
    B.generar_graphviz()

if __name__ == '__main__':
    main()
