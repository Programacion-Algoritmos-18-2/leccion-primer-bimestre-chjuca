class Empleado():								# Creamos la Clase Empleado

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
		self.nombre=nombre

	def obtenerNombre(self):					#Esta funcion devuelve el atributo nombre
		return self.nombre

	def agregarApellido(self,apellido):			#Funcion da valor apellido el atributo apellido
		self.apellido=apellido

	def obtenerApellido(self):					#Esta funcion devuelve el atributo apellido
		return self.cedula

	def agregarCedula(self,cedula):				#Funcion da valor cedula el atributo cedula
		self.cedula=cedula

	def obtenerCedula(self):					#Esta funcion devuelve el atributo cedula
		return self.cedula
	def presentarDatos(self):
		cadena="Informacion de %s %s\n\t CEDULA: %s"%(self.obtenerNombre(),self.apellido,self.obtenerCedula())
		return cadena


		