class Empleado(object):								# Creamos la Clase Empleado

	def __init__(self):							# Creamos el Metodo __init__
		self.nombre = ""						# Atributos de la clase Empleado
		self.apellido = ""
		self.cedula = 0
		self.comision_fija = 0.0

	def agregarComisionFija(self,comision):		#Funcion da valor comision el atributo comision_fija
		self.comision_fija = comision

	def obtenerComisionFija(self):				#Esta funcion devuelve el atributo comision_fija
		return	self.comision_fija

	def agregarNombre(self,nombre):				#Funcion da valor nombre el atributo nombre
		self.nombre = nombre

	def obtenerNombre(self):					#Esta funcion devuelve el atributo nombre
		return self.nombre

	def agregarApellido(self,apellido):			#Funcion da valor apellido el atributo apellido
		self.apellido = apellido

	def obtenerApellido(self):					#Esta funcion devuelve el atributo apellido
		return self.cedula

	def agregarCedula(self,cedula):				#Funcion da valor cedula el atributo cedula
		self.cedula = cedula

	def obtenerCedula(self):					#Esta funcion devuelve el atributo cedula
		return self.cedula

	def presentarDatos(self):
		cadena = "Informacion de %s %s\n\t CEDULA: %s" % (self.obtenerNombre(),self.apellido,self.obtenerCedula())
		return cadena


class EmpleadoPorHoras(Empleado):				# Creamos la Clase EmpleadoporHoras hijo de Empleados

	def __init__(self):								# Creamos el Metodo __init__
		super(EmpleadoPorHoras, self).__init__()	# Herencia de Atributos de la clase Empleado
		self.numeroHoras = 0						# Atributos de la clase EmpleadoporHoras
		self.valorHora = 0.0

	def agregarNumeroHoras(self,horas):				#Funcion da valor horas el atributo numeroHoras		
		self.numeroHoras=horas

	def obtenerNumeroHoras(self):					#Esta funcion devuelve el atributo numeroHoras
		return self.numeroHoras

	def agregarValorHora(self,valor):				#Funcion da valor el atributo valorHoras		
		self.valorHora = valor

	def obtenerValorHora(self):						#Esta funcion devuelve el atributo valorHora
		return self.valorHora

	def calcularValorSueldoFinal(self):				#Esta Funcion Calcula el sueldo final que recibra el Empleado
		sueldoFinal = (self.numeroHoras*self.valorHora)+self.obtenerComisionFija()
		return sueldoFinal

	def presentarDatos(self):						# Presentamos Datos
		cadena = "%s\nNumero Horas: %d\nValor Hora: %.2f\nSueldo Final: %.2f" % (super(EmpleadoPorHoras,self).presentarDatos(),self.obtenerNumeroHoras(),self.obtenerValorHora(),self.calcularValorSueldoFinal())
		return cadena	

class EmpleadoFijo(Empleado):						# Creamos la Clase EmpleadoFijo hijo de Empleados

	def __init__(self):								# Creamos el Metodo __init__
		super(EmpleadoFijo, self).__init__()		# Herencia de Atributos de la clase Empleado
		self.sueldoFijo = 0							# Atributos de la clase EmpleadoFijo
		self.descuentoSeguro = 0

	def agregarSueldoFijo(self,sueldo):				#Funcion da valor sueldo el atributo sueldoFijo	
		self.sueldoFijo = sueldo

	def obtenerSueldoFijo(self):					#Esta funcion devuelve el atributo sueldoFijo	
		return self.sueldoFijo
	
	def agregarDescuentoSeguro(self,desc):			#Funcion da valor sueldo el atributo descuentoSeguro
		self.descuentoSeguro = desc

	def obtenerDescuentoSeguro(self):				#Esta funcion devuelve el atributo descuentoSeguro
		return self.descuentoSeguro

	def calcularSueldoFinal(self):					# Calculamos el SueldoFinal
		return (self.obtenerSueldoFijo()*(100-self.obtenerDescuentoSeguro())) + self.obtenerComisionFija()

	def presentarDatos(self):						# Presentamos Datos
		cadena = ("%s\nSueldo Fijo: %.2f\nDescuento Seguro: %.2f\nSueldo Final: %.2f\n" % (super(EmpleadoFijo, self).presentarDatos(), self.obtenerSueldoFijo(), self.obtenerDescuentoSeguro(), self.calcularSueldoFinal()))
		return cadena

class EmpleadoPorSemana(Empleado):					# Creamos la Clase EmpleadoPorSemana hijo de Empleados
		
	def __init__(self):								# Creamos el Metodo __init__
		super(EmpleadoPorSemana, self).__init__()	# Herencia de Atributos de la clase Empleado
		self.numeroSemanas = 0						# Atributos de la clase EmpleadoPorSemana
		self.valorSemanal = 0

	def agregarNumeroSemanas(self, semanas):		#Funcion da valor ssemanas el atributo numeroSemanas
		self.numeroSemanas = semanas

	def obtenerNumeroSemanas(self):					#Esta funcion devuelve el atributo numeroSemanas
		return numeroSemanas

	def agregarValorSemanal(self, valor):			#Funcion da valor el atributo valorSemanal
		self.valorSemanal = valor

	def obtenerValorSemanal(self):					#Esta funcion devuelve el atributo valorSemanal
		return valorSemanal

	def calcularSueldoFinal(self):					# Calcula el sueldo Final
		return self.obtenerNumeroSemanas() * self.obtenerValorSemanal() + self.obtenerComisionFija()

	def presentarDatos(self):						# Se presenta Datos
		cadena = ("%s\nNumero Semanas: %.2f\nValor semanal: %.2f\nSueldo final: %.2f\n"  % (super(EmpleadoPorSemana, self).presentarDatos(), self.obtenerNumeroSemanas(), self.obtenerValorSemanal(), self.calcularSueldoFinal()))
		return cadena