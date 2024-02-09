class pila:
    def __init__(self):
        self.elemento=[]

    def push(self, dato):
        self.elemento.append(dato)

    def pop(self):
        if(len(self.elemento)==0):
            return "Pila Vacia"
        else:
            return self.elemento.pop()

mipila = pila()
mipila.push("Primer Valor")
mipila.push("Segundo Valor")
mipila.push("Tercer Valor")
mipila.push("Cuarto Valor")
print(mipila.pop())
print(mipila.pop())
print(mipila.pop())
print(mipila.pop())
print(mipila.pop())
print(mipila.pop())
print(mipila.pop())
