import calendar

class Empleado (object):
    nombre=None
    apellido=None
    telefono=None
    fecha_nac=None

    def  __init__(self):
        self.dias_que_debe_ir = [False, True, True, True, True, True, False]

    def __init__(self):
        self.dias_concurridos= []

    def AgregarNombre (self,nombre):
        set.nombre=nombre

    def AgregarApellido (self,apellido):
        set.apellido=apellido

    def AgregarTelefono (self,telefono):
        set.telefono=telefono

    def AgregarFecha_Nac (self,fecha_nac):
        set.fecha_nac=fecha_nac

    def DiasConcurridos (self):
        for item in dias_que_debe_ir:
            if dias_que_debe_ir[item] == True:
                self.dias_concurridos.append(dias_que_debe_ir)

    def DiasQueDebeir (self,año,mes):
        cdias_que_fue=0
        cdias_q_tiene_q_ir=0
        cant_dias_mes=calendar.monthrange(año,mes)
        for i in range (1,cant_dias_mes+1):
            fecha=datetime.date(año,mes,i)
            if fecha==item:
                cdias_que_fue +=1
                break
            cdias_q_tiene_q_ir += 1
        return cdias_que_fue/cdias_q_tiene_q_ir

    def Porcentaje (self):
        suma=0
        for item in self.empleados:
            suma+=item.porcentaje(año,mes)
        return suma/len(self.empleados)





















