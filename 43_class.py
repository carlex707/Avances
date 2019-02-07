class Perro:
    def __init__(self,nombre):
        self.nombre=()
        self.trucos = []

    def agregar_Truco(self,truco):
        self.trucos.append(truco)

f = Perro('Fido')
f.agregar_Truco('Darse la vuelta')

n = Perro('Negro')
f.agregar_Truco('hacerse el muerto')

print(f.trucos)