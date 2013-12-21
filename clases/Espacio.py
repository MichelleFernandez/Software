#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# Espacio.py
# Clase que representa un espacio.
#
# Autores: 
#	   Carla Barazarte, 08-10096.
#	   Alejandro Garbi, 08-10398.
# 	   Michelle Fernandez, 09-10279.
#	   Jose Figueredo, 10-10245.
#	   Alejandro Guillen, 10-10333.
#	   Donato Rolo, 10-10640.
# ------------------------------------------------------------

class Espacio:
  def __init__(self):
    self.id = raw_input("Id: ")
    self.nombre = raw_input("Nombre: ")
    self.ubicacion = raw_input("Ubicacion: ")
    self.capacidad = raw_input("Capacidad maxima: ")

  def get_id(self):
    return self.id
  
  def set_id(self, id):
    self.id = id
    
  def get_nombre(self):
    return self.nombre
  
  def set_nombre(self, nombre):
    self.nombre = nombre
    
  def get_ubicacion(self):
    return self.ubicacion
  
  def set_ubicacion(self, ubicacion):
    self.ubicacion = ubicacion
    
  def get_capacidad(self):
    return self.capacidad
  
  def set_capacidad(self, capacidad):
    self.capacidad = capacidad
    
  def to_string(self):
     print
     print("Id: " + self.id)
     print("Nombre: " + self.nombre)
     print("Ubicacion: " + self.ubicacion)
     print("capMax: " + self.capacidad)
     print