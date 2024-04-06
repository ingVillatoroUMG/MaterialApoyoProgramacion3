import graphviz

class nodoArbol:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.valor = valor

class ABB:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        self.raiz = self._insert(valor, self.raiz)

    def _insert(self, valor, nodo):
        if nodo is None:
            return nodoArbol(valor)
        
        if(valor < nodo.valor):
            nodo.izq = self._insert(valor, nodo.izq)
        elif(valor > nodo.valor):
            nodo.der = self._insert(valor, nodo.der)
        
        self._balancear(valor, nodo)
        
        return nodo

    def _balancear(self, valor, nodo):

        nodo.height = 1 + max(self._get_height(nodo.left), self._get_height(nodo.right))
        balance = self._get_balance(nodo)

        # Caso de rotación simple a la derecha
        if balance > 1 and valor < nodo.left.key:
            return self._rotate_right(nodo)

        # Caso de rotación simple a la izquierda
        if balance < -1 and valor > nodo.right.key:
            return self._rotate_left(nodo)

        # Caso de rotación doble a la derecha-izquierda
        if balance > 1 and valor > nodo.left.key:
            nodo.left = self._rotate_left(nodo.left)
            return self._rotate_right(nodo)

        # Caso de rotación doble a la izquierda-derecha
        if balance < -1 and valor < nodo.right.key:
            nodo.right = self._rotate_right(nodo.right)
            return self._rotate_left(nodo)

    def _get_height(self, nodo):
        if not nodo:
            return 0
        return nodo.height

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_height(nodo.left) - self._get_height(nodo.right)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y



    def buscar(self, valor, nodo):
        if nodo is None:
            print("No encontrado")
            return nodoArbol(-1) 
        if nodo.valor == valor:
            return nodo
        if(valor<nodo.valor):
            return self.buscar(valor, nodo.izq)
        else:
            return self.buscar(valor, nodo.der)
    
    def inorder(self, nodo):
        if nodo !=None:
            self.inorder(nodo.izq)
            print(nodo.valor)
            self.inorder(nodo.der)

    def preorder(self, nodo):
        if nodo !=None:
            print(nodo.valor)
            self.inorder(nodo.izq)
            self.inorder(nodo.der)

    def postorder(self, nodo):
        if nodo is None:
            return
        
        ultimo_nodo_visitado = None
        while nodo:
            if nodo.izq and nodo.izq != ultimo_nodo_visitado and nodo.der != ultimo_nodo_visitado:
                nodo = nodo.izq
            elif nodo.der and nodo.der != ultimo_nodo_visitado:
                nodo = nodo.der
            else:
                print(nodo.valor)
                ultimo_nodo_visitado = nodo
                nodo = nodo.padre

    def mostrar(self, nodo):
        if nodo != None:
            if nodo.izq != None:
                print(nodo.valor, "-> ", nodo.izq.valor)
            if nodo.der != None:
                print(nodo.valor, "-> ", nodo.der.valor)
            self.mostrar(nodo.izq)
            self.mostrar(nodo.der)

    def  generar_arbol_grafico(self):
        dot = graphviz.Digraph()
        self._generar_arbol_grafico(self.raiz, dot)

        archivo_salida = "arbol.dot"
        dot.render(archivo_salida, format='png', cleanup=True)

    def _generar_arbol_grafico(self, nodo, dot):
        if nodo is not None:
            dot.node(str(nodo.valor))
            if nodo.izq is not None:
                dot.edge(str(nodo.valor), str(nodo.izq.valor))
                self._generar_arbol_grafico(nodo.izq, dot)
            if nodo.der is not None:
                dot.edge(str(nodo.valor), str(nodo.der.valor))
                self._generar_arbol_grafico(nodo.der, dot)

    def delete(self, valor):
        self.raiz = self._delete(self.raiz, valor)

    def _delete(self, node, valor):
        if node is None:
            return node

        if valor < node.valor:
            node.izq = self._delete(node.izq, valor)
        elif valor > node.valor:
            node.der = self._delete(node.der, valor)
        else:
            if node.izq is None:
                return node.der
            elif node.der is None:
                return node.leizqft

            node.valor = self._find_min(node.der).valor
            node.right = self._delete(node.der, node.valor)

        return node

    def _find_min(self, node):
        while node.izq is not None:
            node = node.izq
        return node
    
    def _find_max(self, node):
        while node.der is not None:
            node = node.der
        return node              
