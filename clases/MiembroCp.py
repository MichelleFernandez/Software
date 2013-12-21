#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3
# Miembro_CP.py
# Clase que representa un Miembro CP.
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
from Inscrito import *

class MiembroCp(Inscrito):
    def __init__(self):
      Inscrito.__init__(self)
      
      self.experticias = []
      self.articulos = []
      
      
    def get_experticias(self):
      return self.experticias
      
    def get_articulos(self):
      return self.articulos
    
    def remover_articulo(self, titulo):
      articulos = self.get_articulos()
      x = -1
      fin = False
      
      while (x < len(articulos)) and not fin:
	x += 1
	fin = (articulos[x] == titulo)
	
      self.articulos.remove(articulos[x])
    
    def print_articulos(self):
      for x in range(len(self.articulos)):
	print '%s %d %s %s' %("[", x, "]", self.articulos[x])
    
    def agregar_experticia(self, topicos):
      self.experticias.append(topicos)
      
    def print_experticias(self):
      experticias = self.experticias
      for x in range(len(experticias)):
	print '%s%d%s' % ("[", x, "] " + str(experticias[x])) 