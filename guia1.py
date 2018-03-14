class Alumno (object):
    nombre=None
    apellido=None
    fecha_nacimiento=None

    def __init__(self):
        self.listanotas = []

    def setNombre (self,nombre):
        self.nombre = nombre
    def setApellido (self,apellido):
        self.apellido = apellido
    def setFecha_nacimiento (self,fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def setAgregarnota(self,notas):

        if notas>10:
            return False
        if notas<1:
            return False
        self.listanotas.append(notas)
        return True

    def getNotaMayor(self):
        return max(self.listanotas)

    def getNotaMenor(self):
        return min(self.listanotas)

    def getPromedio(self):
        return sum(self.listanotas)/len(self.listanotas)


