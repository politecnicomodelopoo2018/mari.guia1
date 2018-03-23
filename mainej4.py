from clase_empleado import Empresa
from ejer4 import Empleado
import datetime


a= Empresa()
empleado =  Empleado()

empleado.nombre= input ("ingrese nombre ")
empleado.apellido=input ("ingrese apellido ")
empleado.telefono= input ("ingrese telefono ")
empleado.fecha_nac= datetime.date(2000,10,23)

print(empleado.Porcentaje())




