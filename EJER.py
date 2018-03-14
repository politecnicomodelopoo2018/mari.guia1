from guia1 import Alumno
import datetime


a=Alumno()
a.setNombre("Marisol")
a.setApellido("Reynoso")
unaF = datetime.date(2000,12,1)
a.setFecha_nacimiento(unaF)
a.setAgregarnota(8)
a.setAgregarnota(7)
print("Nombre: ", a.nombre)
print("Apellido: ", a.apellido)
print("Fecha Nacimiento: ", a.fecha_nacimiento)
print("Notas: ", a.listanotas)
print("Nota mayor: ", a.getNotaMayor())
print("Nota menor: ", a.getNotaMenor())
print("Promedio: ", a.getPromedio())