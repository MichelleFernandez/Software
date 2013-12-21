#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 2

# test.py
# Modulo de pruebas.
#
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
# ------------------------------------------------------------

import unittest

from clases.Conferencia import *
from clases.CP import *
from clases.Articulo import *
from clases.Inscrito import *
from clases.Miembro_CP import *
from clases.Evento import *
from clases.Espacio import *

class test(unittest.TestCase):

  # INICIALIZACIONES
  
  def setUp(self):
    
    # Articulo
    self.articulo = Articulo()
    self.articulo.titulo = "Articulo de Luis Perez"
    self.articulo.topico_principal.append("Base de Datos")
    self.articulo.topicos_secundarios.append("Inteligencia Artificial")
    self.articulo.autores = "Luis Perez"
    self.articulo.palabra_clave = "Perez"
    self.articulo.num_evaluaciones = 0
    self.articulo.num_evaluadores = 3
    self.articulo.puntuacion = 15
    self.articulo.promedio = 5.0
    self.articulo.texto = "Es es el articulo de Luis Perez"
    
    # Conferencia
    self.conferencia = Conferencia()
    self.conferencia.nombre = "Conferencia Latinoamericana de Informatica"
    self.conferencia.siglas = "CLEI"
    self.conferencia.topicos = ["Inteligencia Artificial", "Base de Datos", "Lenguajes de Programacion"]
    self.conferencia.max_articulos = 5
    self.conferencia.articulos = ["Articulo de Luis Perez", "Articulo de Donato Rolo"]
    self.conferencia.aceptables =  ["Articulo de Luis Perez", "Articulo de Donato Rolo"]
    self.conferencia.aceptados = ["Articulo de Luis Perez"]
    self.conferencia.empatados = []
    self.conferencia.pres_articulos = False
    self.conferencia.cp = None
    self.conferencia.inscritos = ["Luis Perez", "Donato Rolo"]
    
    # CP
    self.cp = CP()
    self.cp.presidente = "Michelle Fernandez"
    self.cp.miembros = ["Michelle Fernandez", "Donato Rolo"]
    
    # Inscrito
    self.inscrito = Inscrito()
    self.inscrito.nombre = "Donato"
    self.inscrito.apellido = "Rolo"
    self.inscrito.pais = "Venezuela"
    self.inscrito.institucion = "Universidad Simon Bolivar"
    self.inscrito.correo = "donatrolo@gmail.com"
    self.inscrito.dir_postal = 1060
    self.inscrito.url = "www.ldc.usb.ve/~donato"
    self.inscrito.telefono = 2639194
    self.inscrito.participacion = ["Miembro_CP"]
    
    # Miembro_CP
    self.miembro_cp = Miembro_CP()
    self.miembro_cp.experticias = ["Base de Datos", "Lenguajes de Programacion"]
    self.miembro_cp.articulos = ["Articulo de Luis Perez", "Articulo de Donato Rolo"]
   
    # Espacio
    self.espacio = Espacio()
    self.espacio.id = 444
    self.espacio.nombre = "Modulo 5"
    self.espacio.ubicacion = "Conjunto de Auditorios"
    self.capacidad = 150
   
    # Evento
    self.evento = Evento()
    self.evento.id = 1
    self.evento.nombre = "Apertura de CLEI"
    self.evento.tipo = "Social"
    self.evento.duracion = 180
    self.evento.fecha = "07/10/2014"
    self.evento.hora_inicio = "7:30am"
    self.evento.lugar = "001"
   
   
  # TESTING
  
  def test_conferencia(self):
     
    topicos = ["Inteligencia Artificial", "Base de Datos", "Lenguajes de Programacion"]
    articulos = ["Articulo de Luis Perez", "Articulo de Donato Rolo"]
    aceptables = ["Articulo de Luis Perez", "Articulo de Donato Rolo"]
    aceptados = ["Articulo de Luis Perez"]
    empatados = []
    inscritos = ["Luis Perez", "Donato Rolo"]
    eventos = []

    self.assertEqual(self.conferencia.getNombre(), 'Conferencia Latinoamericana de Informatica', "Fallo el getter de nombre.")
    self.assertEqual(self.conferencia.getSiglas(), 'CLEI', "Fallo el getter de siglas.")
    self.assertEqual(self.conferencia.getTopicos(), topicos, "Fallo el getter de topicos.") 
    self.assertEqual(self.conferencia.getMax_articulos(), 5, "Fallo el getter de max_articlos.") 
    self.assertEqual(self.conferencia.getArticulos(), articulos, "Fallo el getter de articulos.") 
    self.assertEqual(self.conferencia.getAceptables(), aceptables, "Fallo el getter de aceptables.") 
    self.assertEqual(self.conferencia.getAceptados(), aceptados, "Fallo el getter de aceptados.") 
    self.assertEqual(self.conferencia.getEmpatados(), empatados, "Fallo el getter de empatados.") 
    self.assertEqual(self.conferencia.getPres_articulos(), False, "Fallo el getter de pres_articulos.") 
    self.assertEqual(self.conferencia.getCp(), None, "Fallo el getter de cp.") 
    self.assertEqual(self.conferencia.getInscritos(), inscritos, "Fallo el getter de inscritos.") 
    self.assertEqual(self.conferencia.getEventos(), eventos, "Fallo el getter de eventos.")  
     
  def test_cp(self):
    
    miembros = ["Michelle Fernandez", "Donato Rolo"]
    
    self.assertEqual(self.cp.getPresidente(), 'Michelle Fernandez', "Fallo el getter de presidente")
    self.assertEqual(self.cp.getMiembros(), miembros, "Fallo el getter de miembros")

    
  def test_articulo(self):
    
    topico_principal = ["Base de Datos"]
    topicos_secundarios = ["Inteligencia Artificial"]
    
    self.assertEqual(self.articulo.getTitulo(), 'Articulo de Luis Perez', "Fallo getter de titulo.")
    self.assertEqual(self.articulo.getTopico_principal(), topico_principal, "Fallo getter de topico_principal.")
    self.assertEqual(self.articulo.getTopicos_secundarios(), topicos_secundarios, "Fallo getter de topicos_secundarios.")
    self.assertEqual(self.articulo.getAutores(), 'Luis Perez', "Fallo getter de autores.")
    self.assertEqual(self.articulo.getPalabra_clave(), 'Perez', "Fallo getter de palabra_clave.")
    self.assertEqual(self.articulo.getNum_evaluaciones(), 0, "Fallo getter de num_evaluaciones.")
    self.assertEqual(self.articulo.getNum_evaluadores(), 3, "Fallo getter de num_evaluadores.")
    self.assertEqual(self.articulo.getPuntuacion(), 15, "Fallo getter de puntuacion.")
    self.assertEqual(self.articulo.getPromedio(), 5.0, "Fallo getter de promedio.")
    self.assertEqual(self.articulo.getTexto(), 'Es es el articulo de Luis Perez', "Fallo getter de texto.")
    
    
  def test_inscrito(self):
    
    participacion = ["Miembro_CP"]
    
    self.assertEqual(self.inscrito.getNombre(), 'Donato', "Fallo getter de nombre.")
    self.assertEqual(self.inscrito.getApellido(), 'Rolo', "Fallo getter de apellido.")
    self.assertEqual(self.inscrito.getPais(), 'Venezuela', "Fallo getter de pais.")
    self.assertEqual(self.inscrito.getInstitucion(), 'Universidad Simon Bolivar', "Fallo getter de institucion.")
    self.assertEqual(self.inscrito.getCorreo(), 'donatrolo@gmail.com', "Fallo getter de correo.")
    self.assertEqual(self.inscrito.getDir_postal(), 1060, "Fallo getter de dir_postal.")
    self.assertEqual(self.inscrito.getUrl(), 'www.ldc.usb.ve/~donato', "Fallo getter de url.")
    self.assertEqual(self.inscrito.getTelefono(), 2639194, "Fallo getter de telefono.")
    self.assertEqual(self.inscrito.getParticipacion(), participacion, "Fallo getter de participacion.")
    
    
  def test_miembro_cp(self):
    
    experticias = ["Base de Datos", "Lenguajes de Programacion"]
    articulos = ["Articulo de Luis Perez", "Articulo de Donato Rolo"]    
    
    self.assertEqual(self.miembro_cp.getExperticias(), experticias, "Fallo getter de experticias.")
    self.assertEqual(self.miembro_cp.getArticulos(), articulos, "Fallo getter de articulos.")
  
  def test_espacio(self):
    self.assertEqual(self.espacio.get_id(), 444, "Fallo getter de id")
    self.assertEqual(self.espacio.get_nombre(), "Modulo 5", "Fallo getter de nombre")
    self.assertEqual(self.espacio.get_ubicacion(), "Conjunto de Auditorios", "Fallo getter de ubicacion")
    self.assertEqual(self.espacio.capacidad(), 150, "Fallo getter de capacidad")
  
  def test_evento(self):
    self.assertEqual(self.evento.get_id(), 1, "Fallo getter de Id.")
    self.assertEqual(self.evento.get_nombre(), "Apertura de CLEI", "Fallo getter de Nombre.")
    self.assertEqual(self.tipo.get_tipo(), "Social", "Fallo getter de Tipo.")
    self.assertEqual(self.evento.get_duracion(), 180, "Fallo getter de Duracion.")
    self.assertEqual(self.evento.get_fecha(), "07/10/2014", "Fallo getter de Fecha.")
    self.assertEqual(self.evento.get_hora_inicio(), "7:30am", "Fallo getter de Hora de Inicio.")
    self.assertEqual(self.evento.get_lugar(), "f001", "Fallo getter de Lugar.")
    

    
if __name__== "__main__":
  unittest.main()