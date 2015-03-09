__author__ = 'Jesús'
from algoritmos.Procesos import *


class Procesador:
	def __init__(self, n):
		self.ls = ListaProcesos(5)
		self.actual = None

	def mostrarLista(self):
		print(self.ls)

	def procesar(self):
		try:
			self.ls.ordenar()
			self.actual = self.ls.extraer()
			print(self.actual.procesar())
			if self.actual.tiempo > 0:
				self.ls.agregar(self.actual)
		except IndexError:
			print("Lista de procesos vacía")