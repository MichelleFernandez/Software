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
from Conferencia import *

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


    def gestionar_empatados(self, conf):
      print
      print("GESTION DE ARTICULOS EMPATADOS")
      print("------------------------------")
      print
      
      cupos_ocupados = len(conf.get_aceptados())
      cupos_restantes = conf.get_max_articulos() - cupos_ocupados

      empatados = conf.get_empatados()
      aceptados = conf.get_aceptados()
      rechazados = conf.get_rechazados()
      
      # Seleccion de los articulos aceptados de entre los empatados.
      while (cupos_restantes > 0):
        #print_articulos(conf.empatados)
        print '%d %s' % (cupos_restantes, " cupo(s) restante(s).")
        fin = False
        while not fin:
	  ans = raw_input(">> ")
          if ans.isdigit():
            ans = int(ans)
            fin = (ans < len(empatados) and (ans >= 0))
        
        articulo = empatados[ans]
        articulo.set_estado_final(1)
        aceptados.append(articulo)

        # Eliminar articulo de la lista de empatados.
        del empatados[ans]

        cupos_restantes -= 1

      # El resto de los articulos que quedan en la lista de empatados se marcan
      # como rechazados por falta de cupo y se colocan en la lista de rechazados
      for x in range(len(empatados)):
        empatado = empatados[x]
        empatado.set_estado_final(3)
        rechazados.append(empatado)

      # Se vacia la lista de empatados
      del empatados[:]

      # Calculadas las listas, se actualizan las listas de la conferencia.
      conf.set_aceptados(aceptados)
      conf.set_empatados(empatados)
      conf.set_rechazados(rechazados)

