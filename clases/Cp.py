#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# CP.py
# Clase que representa un Comite de Programa.

# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
from MiembroCp import *

class Cp:
    def __init__(self):
      self.presidente = None
      self.miembros = []
      
    def get_presidente(self):
      return self.presidente
      
    def set_presidente(self, presidente):
      self.presidente = presidente
      
    def set_miembros(self, miembros):
      self.miembros = miembros
      
    def get_miembros(self):
      return self.miembros
    
    def agregar_presidente(self, presidente):
      self.presidente = presidente
      if len(self.miembros) == 0:
	self.miembros.append(presidente)
      else:
	self.miembros[0] = presidente
    
    def agregar_miembro(self, miembro):
      self.miembros.append(miembro)
    
    def agregar_miembros(self):
      fin = False
      miembros = self.miembros
      
      while not(fin):
	miembro = MiembroCp()
	miembro.set_participacion("Miembro CP")

	if not (len(miembros) == 0):
	  x = 0
	  while (x < len(miembros)) and not (miembros[x].get_correo() == miembro.get_correo()):
	    x += 1
	
	  if not (x == len(miembros)):
	    print("-----------------------")    
	    print("Este usuario ya existe.") 
	    print("-----------------------")
	    continue
	  else:
	    self.miembros.append(miembro)
	    
	else:
	  self.miembros.append(miembro)
	
	print
	ans = raw_input("Desea agregar otro miembro? (S/N) ")
	fin = ans in ["n", "N"]
	print
	
      return miembros
	
    def eliminar_miembro(self, miembro):
      if not (len(self.miembros) == 0):
	self.miembros.remove(miembro)
	
    def to_string(self):
      print("MIEMBROS DEL COMITE DE PROGRAMA")
      print("-------------------------------")
      print
      print("PRESIDENTE")
      print("----------")
      self.presidente.to_string()
      print("----------")
      print
      
      for x in range(1, len(self.miembros)):
	self.miembros[x].to_string()
	print
