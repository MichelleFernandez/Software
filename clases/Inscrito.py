#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# Inscrito.py
# Clase que representa un Inscrito.
#
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
from AsistenciaCharla import *
from AsistenciaTaller import *
from AsistenciaCharlaTaller import *
from Descuento import *
from Academico import *
from CompraTemprana import *
from TipoInscripcion import *
class Inscrito:
    def __init__(self, tipo_inscripcion = None):
      self.nombre = raw_input("Nombre: ")
      self.apellido = raw_input("Apellido: ")
      self.pais = raw_input("Pais: ")
      self.institucion = raw_input("Institucion: ")
      self.correo = raw_input("correo: ")
      
      self.dir_postal = raw_input("Direccion postal: ")
      while not (self.dir_postal.isdigit()):
	print ("Direccion postal no valida.")
	self.dir_postal = raw_input("Direccion postal: ")
	
      self.dir_postal = int(self.dir_postal)
      
      self.url = raw_input("URL: ")
      
      self.telefono = raw_input("Telefono: ")
      
      while not (self.telefono.isdigit()):
	print ("Telefono no valido.")
	self.telefono = raw_input("Telefono: ")

      self.participacion = []
      print
      print("Participacion: ")
      print
      print("[0] Autor")
      print
      print("[1] Asistente")
      print
      print("[2] Charlista invitado")
      print
      ans = raw_input(">> ")
      while not (ans == "0") and not (ans == "1") and not (ans == "") and not (ans == "2"):
	ans = raw_input(">> ")
	
      if ans == "0":
	self.participacion.append("Autor")
      elif ans == "1":
	self.participacion.append("Asistente")
      elif ans == "2":
	self.participacion.append("Invitado")
      print
      #Paquetes de inscripcion
      print("Tipo de Inscripcion: ")
      print
      print("[0] Asistencia exclusiva a charlas")
      print
      print("[1] Asistencia exclusiva a talleres")
      print
      print("[2] Asistencia a talleres y charlas")
      print
      print("[3] Descuentos")
      print
      ans = raw_input(">> ")
      while not (ans == "0") and not (ans == "1") and not (ans == "2") and not (ans == "3"):
            ans = raw_input(">> ")
      if ans == "0":
        self.inscrip = TipoInscripcion(AsistenciaCharla())
      if ans == "1":
        self.inscrip = TipoInscripcion(AsistenciaTaller())
      if ans == "2":
        self.inscrip = TipoInscripcion(AsistenciaCharlaTaller())
      if ans == "3":
        print
        print("[0] Descuento para academicos")
        print
        print("[1] Descuento para compras tempranas")
        print
        ans = raw_input(">> ")
        while not (ans == "0") and not (ans == "1") and not (ans == ""):
            ans = raw_input(">> ")
        if ans == "0":
            self.inscrip = TipoInscripcion(Descuento(Academico()))
        if ans == "1":
            self.inscrip = TipoInscripcion(Descuento(CompraTemprana()))
      self.inscrip=self.inscrip.inscripcion()
    
    def get_nombre(self):
      return self.nombre
      
    def get_apellido(self):
      return self.apellido
     
    def get_pais(self):
      return self.pais
      
    def get_institucion(self):
      return self.institucion
	
    def get_correo(self):
      return self.correo
	
    def get_dir_postal(self):
      return self.dir_postal

    def get_url(self):
      return self.url
    
    def get_telefono(self):
      return self.telefono
      
    def get_participacion(self):
      return self.participacion
      
    def set_participacion(self, participacion):
      self.participacion = []
      self.participacion.append(participacion)
      
    def agregar_participacion(self, participacion):
      self.participacion.append(participacion)
      
    def print_participacion(self):
      participacion = self.participacion
      print
      for x in range(len(participacion)):
	print '%s%d%s' % ("[", x, "] " + participacion[x])
	print
     
    def to_string(self):
      print("Nombre: " + self.nombre)
      print("Apellido: " + self.apellido)
      print("Pais: " + self.pais)
      print("Institucion: " + self.institucion)
      print("Correo: " + self.correo)
      print("Tipo de Inscripcion: " + self.inscrip)