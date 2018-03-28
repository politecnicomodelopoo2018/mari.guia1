import datetime

class Alumno (object):
    nombre=None
    apellido=None
    fec_nac=None

    def __init__(self):
        self.lista_notas = []

    def setNombre(self, nombre):
        self.nombre=nombre.title()

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido=apellido.title()

    def getApellido(self):
        return self.apellido

    def setFecha_nac(self, date):
        self.fec_nac = date


    def getFecha_nac (self):
        return self.fec_nac


