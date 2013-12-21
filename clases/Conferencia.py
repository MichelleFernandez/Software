#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 2

# Conferencia.py
# Clase que representa una conferencia.
#
# Autores: 
#	   Carla Barazarte, 08-10096.
#	   Alejandro Garbi, 08-10398.
# 	   Michelle Fernandez, 09-10279.
#	   Jose Figueredo, 10-10245.
#	   Alejandro Guillen, 10-10333.
#	   Donato Rolo, 10-10640.
# ------------------------------------------------------------

class Conferencia:
    def __init__(self):
      self.nombre = None
      self.siglas = None
      self.topicos = []
      self.max_articulos = None
      
      self.articulos = []
      self.aceptables = []
      self.aceptados = []
      self.empatados = []      
      
      self.pres_articulos = False
      self.cp = None
      self.inscritos = []

      self.eventos = []
      
      self.espacios = []
      
    def get_nombre(self):
      return self.nombre
      
    def set_nombre(self, nombre):
      self.nombre = nombre
      
    def get_siglas(self):
      return self.siglas
      
    def set_siglas(self, siglas):
      self.siglas = siglas
    
    def set_pres_articulos(self, pres_articulos):
      self.pres_articulos = pres_articulos
      
    def get_pres_articulos(self):
      return self.pres_articulos
    
    def get_cp(self):
      return self.cp
    
    def set_topicos(self, topicos):
      self.topicos = topicos
      
    def get_topicos(self):
      return self.topicos
    
    def get_max_articulos(self):
      return self.max_articulos
      
    def set_max_articulos(self, max_articulos):
      self.max_articulos = max_articulos
  
    def get_articulos(self):
      return self.articulos
  
    def set_articulos(self, articulos):
      self.articulos = articulos
   
    def get_aceptados(self):
      return self.aceptados
  
    def set_aceptados(self, articulos):
      self.aceptados = articulos
      
    def get_empatados(self):
      return self.empatados
  
    def set_empatados(self, empatados):
      self.empatados = empatados   
      
    def get_aceptables(self):
      return self.aceptables
  
    def set_aceptables(self, aceptables):
      self.aceptables = aceptables
      
    def get_articulo(self, num):
      return self.articulos[num]

    def get_inscritos(self):
      return self.inscritos
      
    def get_eventos(self):
      return self.eventos
      
    def agregar_evento(self,evento):
      self.eventos.append(evento)

    def get_espacios(self):
      return self.espacios

    def agregar_espacio(self, espacio):
      self.espacios.append(espacio)

    def encontrar_articulo(self, articulo):
      articulos = self.articulos
      
      x = 0
      while (x < len(articulos)) and not (articulos[x].get_titulo() == articulo.get_titulo()):
	x += 1
	
      if (x == len(articulos)):
	return False
	
      return True

    def evaluar(self, titulo, puntos):
      articulos = self.get_articulos()
      x = -1
      fin = False
      
      while (x < len(articulos)) and not fin:
	x += 1
	fin = (articulos[x].get_titulo() == titulo)      

      num_evaluaciones = self.articulos[x].get_num_evaluaciones()
      num_evaluadores = self.articulos[x].get_num_evaluadores()

      self.articulos[x].agregar_puntuacion(puntos)
      self.articulos[x].set_num_evaluaciones(num_evaluaciones + 1)
      self.articulos[x].promediar()
       
      #if (num_evaluaciones == num_evaluadores):
	#print "agregar a la lista de aceptables/rechazados"
	
    def llamar_pres_articulos(self):
      self.set_pres_articulos(True)
      # Avisar a los inscritos.
      
    def fin_pres_articulos(self):
      self.set_pres_articulos(False)
      # Organizar listas de aceptados/empatados
    
    def agregar_inscrito(self, inscrito):
      self.inscritos.append(inscrito)
    
    def calcular_aceptados(self):
      articulos = self.aceptables
      max_articulos = self.max_articulos

      print len(articulos) 
      print (max_articulos)
      
      if (len(articulos) > max_articulos):
	promedio_min = articulos[max_articulos - 1].get_promedio()
      
	if (articulos[max_articulos].get_promedio() == promedio_min):      
	  x = max_articulos - 2
	  while (x >= 0) and (articulos[x].get_promedio() == promedio_min):
	    x -= 1
	    
	  y = x + 1
	  while (y < len(articulos)) and (articulos[y].get_promedio() == promedio_min):
	    y += 1
	    
	  for i in range(x + 1):
	    self.aceptados.append(articulos[i])
	    
	  for i in range(x + 1, y):
	    self.empatados.append(articulos[i])
	    
	else:
	  for x in range(max_articulos):
	    self.aceptados.append(articulos[x])
	  
      else:
	for x in range(len(articulos)):
	  print x
	  self.aceptados.append(articulos[x])
	    
	  # rechazar el resto de los articulos.
    
    #def printTopicos(self):
      #topicos = self.topicos
      #for x in range(len(topicos)):
	#print '%s%d%s' % ("[", x, "] " + topicos[x])
	#print
    
    def toString(self):
      print("CONFERENCIA")
      print("------------")
      print("Nombre: " + self.nombre)
      print("Siglas: " + self.siglas)
      print("Topicos: ")
      print(self.topicos)
      print("------------")      
      if not(self.cp == None):
	self.cp.to_string()
      #self.printArticulos()
      
