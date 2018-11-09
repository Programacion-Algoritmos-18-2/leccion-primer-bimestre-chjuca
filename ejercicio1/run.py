#Crear Empleado
from mipaquete.modelado import *		# Importamos la clase empleado
	
e=Empleado()							# Creamos el Objeto 
e.agregarNombre("Luis")					# Llamamos a la funcion agregarNombre con el parametro "Luis"
e.agregarApellido("Benitez")			# Llamamos a la funcion agregarApellido con el parametro "Benitez"
e.agregarCedula("1110001")				# Llamamos a la funcion agregarCedula con el parametro "1110001"
print(e.presentarDatos())				# Llamamos a la funcion presentarDatos

e1 = EmpleadoPorHoras()					# Creamos el Objeto para la Clase EmpleadoPorHoras
nombre=input("Ingrese su nombre: ")		# Se lee por teclado el Nombre
e1.agregarNombre(nombre)				# Se le da valores a los atributos
e1.agregarApellido("Andrade")
e1.agregarCedula("112233")
e1.agregarNumeroHoras(15)
e1.agregarValorHora(20.2)
print(e1.presentarDatos())				# Se presenta Datos

e2=EmpleadoFijo()						# Creamos el Objeto para la Clase EmpleadoFijo
e2.agregarSueldoFijo(300.2)				#Se le da valor a los atributos
e2.descuentoSeguro = 10
comision = input("Ingrese Comision: ")	# Se lee por teclado el valor de la comision
comision = float(comision)				# Se convierte comision en float
e2.agregarComisionFija(comision)		# Se le da valor a los atributos
e2.nombre = "Ana"
e2.apellido = "Diaz"
print(e2.presentarDatos())