#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# Articulo.py
# Clase que representa un articulo.
#
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
class Articulo:
    def __init__(self):
      self.titulo = raw_input("Titulo: ")
      self.topico_principal = []
      self.topicos_secundarios = []
      self.autores = raw_input("Autor(es): ")
      self.palabra_clave = raw_input("Palabra Clave: ")
      self.num_evaluaciones = 0
      self.num_evaluadores = 0
      self.puntuacion = 0
      self.promedio = 0
      self.texto = raw_input("Texto: ")
      self.pais = raw_input("Pais: ")
      self.estado_final = 0
      self.texto = raw_input("Texto: ")
      
    def get_titulo(self):
      return self.titulo
      
    def set_titulo(self, titulo):
      self.titulo = titulo
      
    def get_topico_principal(self):
      return self.topico_principal
      
    def set_topico_principal(self, topico):
      self.topico_principal = topico

    def get_topicos_secundarios(self):
      return self.topicos_secundarios
      
    def set_topicos_secundarios(self, topicos):
      self.topicos_secundarios = topicos
      
    def get_autores(self):
      return self.autores
      
    def get_palabra_clave(self):
      return self.palabra_clave
      
    def get_num_evaluadores(self):
      return self.num_evaluadores
      
    def set_num_evaluadores(self, num_evaluadores):
      self.num_evaluadores = num_evaluadores
      
    def get_num_evaluaciones(self):
      return self.num_evaluaciones
      
    def set_num_evaluaciones(self, num_evaluaciones):
      self.num_evaluaciones = num_evaluaciones
      
    def set_puntuacion(self, puntuacion):
      self.puntuacion = puntuacion
    
    def get_puntuacion(self):
      return self.puntuacion
    
    def get_promedio(self):
      return self.promedio
    
    def set_promedio(self, promedio):
      self.promedio = promedio
      
    def get_texto(self):
      return self.texto
  
    def get_pais(self):
      return self.pais

    def get_estado_final(self):
      return self.estado_final

    def set_estado_final(self, estado):
      self.estado_final = estado
      
    def agregar_puntuacion(self, puntuacion):
      self.puntuacion += puntuacion
      
    def promediar(self):
      puntuacion = self.get_puntuacion()
      num_eval = self.get_num_evaluaciones()
      self.promedio = round(float(puntuacion / num_eval), 2)

