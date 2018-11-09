#Crear Empleado
from mipaquete.modelado import *		# Importamos la clase empleado
	
e=Empleado()							# Creamos el Objeto 
e.agregarNombre("Luis")					# Llamamos a la funcion agregarNombre con el parametro "Luis"
e.agregarApellido("Benitez")			# Llamamos a la funcion agregarApellido con el parametro "Benitez"
e.agregarCedula("1110001")				# Llamamos a la funcion agregarCedula con el parametro "1110001"
print(e.presentarDatos())				# Llamamos a la funcion presentarDatos