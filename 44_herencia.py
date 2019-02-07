class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_Datos(self):
        return self.nombre + "\t" + self.apellido

class Trabajador(Persona):
    def __init__(self,nombre, apellido, cargo):
        Persona.__init__(self,nombre, apellido)
        self.cargo = cargo 

    def get_Datos(self):
        return Persona.get_Datos(self) + "\t" + self.cargo


p = Persona('Marge','Simpson')
print(p.get_Datos())

t = Trabajador('Homero','Simpson','fronted developer')
print(t.get_Datos()) 