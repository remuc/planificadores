__author__ = "Jesús"

class Prioridad :
	actual = None

	def __init__(self, priori):
		if "A" <= priori <= "E":
			self.actual = priori
		else:
			raise ValueError

	def __int__(self):
		return{
			self.actual == "A": 1,
			self.actual == "B": 2,
			self.actual == "C": 4,
			self.actual == "D": 8,
			self.actual == "E": 16,
		}[True]

	def reducir(self):
		if self.actual == "E":
			None
		else:
			self.actual = chr(ord(self.actual) + 1)


class Proceso:

	def __init__(self, nombre, tiempo, prioridad):
		self.nombre = nombre
		self.tiempo = tiempo
		self.prioridad = Prioridad(prioridad)

	def __str__(self):
		return self.nombre + "\t" + str(self.tiempo) + "\t" + self.prioridad.actual

	def __eq__(self, otro):
		return self.nombre == otro.nombre

	def __lt__(self, otro):
		return self.prioridad.actual < otro.prioridad.actual

	def procesar(self):
		ls = [(self.nombre, tmp)
			for tmp in range(self.tiempo - int(self.prioridad) + 1, self.tiempo +1)
				if tmp > 0]
		ls.reverse()
		self.tiempo -= int(self.prioridad)
		if self.tiempo <= 0:
			raise(Warning)
		self.prioridad.reducir()
		return ls


class ListaProcesos:
	# En su constructor se define el tamaño de la lista y se genera un espacio para poder almacenar ahí los procesos.
	def __init__(self, tamaño):
		self.tamaño = tamaño
		self.procesos = []

	# El método __str__() dice como se convertirá  a cadena la lista (De esta manera se muestra la lista de procesos).
	def __str__(self):
		cadena = ""
		for i in self.procesos:
			cadena += str(i) + "\n"
		return cadena

	# El método agregar(proceso) verifica si hay espacio (IndexError)
	#si no está repetido el proceso (NameError) y si el tiempo es correcto (Arithmetic Error).
	def agregar(self, proceso):
		if len(self.procesos) == self.tamaño:
			raise IndexError
		elif self.procesos.count(proceso) > 0:
			raise NameError
		elif proceso.tiempo <= 0:
			raise ArithmeticError
		else:
			self.procesos.insert(0, proceso)

	# La función extraer() realiza un pop de una lsita.
	def extraer(self) -> Proceso:
		return self.procesos.pop()

	# El método ordenar() es sólo usado para la multiprogramación.
	# En este caso se trata de un burbuja básico,
	# adaptado para funcionar a la hora de operar con procesos (utiliza la sobrecarga de <).
	def ordenar(self):
		for num in range(len(self.procesos) -1, 0, -1):
			for i in range(num):
				if self.procesos[i] < self.procesos[i+1]:
					temp = self.procesos[i]
					self.procesos[i] = self.procesos[i + 1]
					self.procesos[i + 1] = temp