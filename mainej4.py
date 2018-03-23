from clase_empleado import Empresa
from ejer4 import Empleado
import datetime
import calendar

c = calendar.HTMLCalendar(calendar.SUNDAY)
print c.formatmonth(2007, 7)

a= Empresa()
empleado =Empleado()

empleado.nombre= input ("ingrese nombre ")
empleado.apellido=input ("ingrese apellido ")
empleado.telefono= input ("ingrese telefono ")
empleado.fecha_nac= datetime.date(2000,10,23)
por = empleado.Porcentaje()
print(empleado.Porcentaje(2018,3,2))
print(a.)





