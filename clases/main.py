#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 2

# main.py
# Programa principal
#
# Autores: 
#	   Carla Barazarte, 08-10096.
#	   Alejandro Garbi, 08-10398.
# 	   Michelle Fernandez, 09-10279.
#	   Jose Figueredo, 10-10245.
#	   Alejandro Guillen, 10-10333.
#	   Donato Rolo, 10-10640.
# ------------------------------------------------------------

from ctypes import *
import os

from clases.Conferencia import *
from clases.CP import *
from clases.Espacio import *
from clases.Evento import *
from clases.Articulo import *
from clases.Inscrito import *
from clases.Miembro_CP import *
from clases.Programacion import *
        
# ------------------------------------------------------------
#		Funciones y Procedimientos
# ------------------------------------------------------------        

def printArticulos(lista):
  if not (len(lista) == 0):
    print
    for x in range(len(lista)):
      print '%s %d %s %s' % ("[", x, "] Titulo ", lista[x].getTitulo())
      print '%s %d' % ("	Puntuacion: ", lista[x].getPuntuacion())
      print '%s %f' % ("	Promedio: ", lista[x].getPromedio())
      print '%s %d' % ("	Evaluaciones: ", lista[x].getNum_evaluaciones())
      print '%s %d' % ("	Evaluadores: ", lista[x].getNum_evaluadores())
      print  
    print
  else:
    print
    print("-------------------------------")    
    print("La lista no contiene articulos.")
    print("-------------------------------")    
    print

def printTopicos(topicos):
  for x in range(len(topicos)):
    print '%s%d%s' % ("[", x, "] " + topicos[x])
    print     
    
def evaluarPromedio(conf, titulo):
  articulos = conf.getArticulos()
  x = -1
  fin = False

  while (x < len(articulos)) and not fin:
    x += 1
    fin = (articulos[x].getTitulo() == titulo)
 
  num_evaluadores = articulos[x].getNum_evaluadores()
  num_evaluaciones = articulos[x].getNum_evaluaciones()
  promedio = articulos[x].getPromedio()
  max_articulos = conf.getMax_articulos()
 
  if (num_evaluaciones == num_evaluadores):
    if not (promedio <= 2):
      agregarArticulo(conf.getAceptables(), conf.getArticulo(x))
    #else:
      # Rechazar articulo

def agregarArticulo(lista, articulo):
  lista.append(articulo)
   
def setTopicos(topicos):
  print
  printTopicos(topicos)
  
  ans = raw_input(">> ")
  while not (ans.isdigit()):
    ans = raw_input(">> ")
  
  ans = int(ans)  
  
  topicos_selec = []
  topicos_selec.append(topicos[ans])
  
  return topicos_selec
    
        
# ------------------------------------------------------------
# 		Programa Principal
# ------------------------------------------------------------

# Inicializacion de la conferencia.

os.system('clear')

clei = Conferencia()
clei.set_nombre("Conferencia Latinoamericana de Informatica")
clei.set_siglas("CLEI")

topicos = ["Inteligencia Artificial", "Base de Datos", "Lenguajes de Programacion"]
clei.set_topicos(topicos)

clei.set_max_articulos(5)

# Seccion de pruebas.

#articulo0.promedio = 5
#articulo0.num_evaluaciones = 3
#articulo0.num_evaluadores = 3

#articulo1 = Articulo()
#articulo1.promedio = 4
#articulo1.num_evaluaciones = 3
#articulo1.num_evaluadores = 3

#articulo2 = Articulo()
#articulo2.promedio = 3.2
#articulo2.num_evaluaciones = 3
#articulo2.num_evaluadores = 3

#articulo3 = Articulo()
#articulo3.promedio = 3.2
#articulo3.num_evaluaciones = 3
#articulo3.num_evaluadores = 3

#articulo4 = Articulo()
#articulo4.promedio = 3.1
#articulo4.num_evaluaciones = 3
#articulo4.num_evaluadores = 3

#articulo5 = Articulo()
#articulo5.promedio = 3.1
#articulo5.num_evaluaciones = 3
#articulo5.num_evaluadores = 3

#articulo6 = Articulo()
#articulo6.promedio = 2
#articulo6.num_evaluaciones = 3
#articulo6.num_evaluadores = 3

#clei.articulos.append(articulo0)
#clei.articulos.append(articulo1)
#clei.articulos.append(articulo2)
#clei.articulos.append(articulo3)
#clei.articulos.append(articulo4)
#clei.articulos.append(articulo5)
#clei.articulos.append(articulo6)

#print "ARTICULOS RECIBIDOS"
#print "-------------------"
#print
#printArticulos(clei.articulos)

#evaluarPromedio(clei, articulo0.titulo)
#evaluarPromedio(clei, articulo1.titulo)
#evaluarPromedio(clei, articulo2.titulo)
#evaluarPromedio(clei, articulo3.titulo)
#evaluarPromedio(clei, articulo4.titulo)
#evaluarPromedio(clei, articulo5.titulo)
#evaluarPromedio(clei, articulo6.titulo)

#print "ARTICULOS ACEPTABLES"
#print "-------------------"
#print
#printArticulos(clei.aceptables)

#clei.calcularAceptados()

#print "ARTICULOS ACEPTADOS"
#print "-------------------"
#print
#printArticulos(clei.aceptados)
#print

#print "ARTICULOS EMPATADOS"
#print "-------------------"
#print
#printArticulos(clei.empatados)
#print
    
salir = False
while not salir:

  print
  print("Sistema del CLEI")
  print("----------------")
  print  
  print("[0] Administrador")
  print
  print("[1] Inscrito")
  print
  print("[10] Salir")
  print
  
  ans = raw_input(">> ")
  
  os.system('clear')
  
  if (ans == "0"):
    volver = False
    while not volver:
      print
      print("ADMINISTRADOR")
      print("-------------")
      print
      print("[0] Comite de Programa")
      print
      print("[1] Llamar a la Presentacion de Articulos")
      print
      print("[2] Finalizar la Presentacion de Articulos")
      print
      print("[3] Lista de Articulos Recibidos")
      print
      print("[4] Lista de Articulos Aceptables")
      print
      print("[5] Lista de Articulos Aceptados")
      print
      print("[6] Lista de Articulos Empatados")
      print
      print("[7] Registrar Espacio")
      print
      print("[8] Registrar Evento")
      print
      print("[9] Programar Eventos")      
      print
      print("[10] Volver")
      print
      
      ans = raw_input(">> ")
      os.system('clear')

      if (ans == "0"):
	volver = False
	while not(volver):
	  print
	  print("COMITE DE PROGRAMA")
	  print("------------------")
	  print
	  print("[0] Crear Comite")
	  print
	  print("[1] Modificar Presidente")
	  print
	  print("[2] Agregar Miembros")
	  print
	  print("[3] Listar Miembros")
	  print
	  print("[10] Volver")
	  print
	  
	  ans = raw_input(">> ")
	  os.system('clear')
	  
	  if (ans == "0"):
	    clei.cp = CP()
	    
	    print
	    print("PRESIDENTE")
	    print("----------")
	    print
	    
	    presidente = Miembro_CP()
	    presidente.agregar_participacion("Miembro CP")
	    
	    print
	    print("EXPERTICIAS")
	    print("-----------")
	    
	    # Experticias
	    topicos = clei.get_topicos()
	    
	    fin = False
	    while not fin:
	      experticias = set_topicos(topicos)
	    
	      presidente.agregar_experticia(topicos)
	      
	      topicos_disp = topicos
	      #topicos_disp.remove(experticias[0])
	      
	      print
	      ans = raw_input("Desea agregar una nueva experticia? (S/N) ")
	      fin = (ans in ["n", "N"])
	        
	    clei.cp.agregar_presidente(presidente)
	    clei.agregar_inscrito(presidente)
	    
	    os.system('clear')
	    
	    print
	    print("MIEMBROS")
	    print("--------")
	    print
	    
	    miembros = clei.cp.agregar_miembros()
	    
	    os.system('clear')
	    
	    for x in range(len(miembros)):
	      clei.agregar_inscrito(miembros[x])
	    
	  elif (ans == "1"):
	    if (clei.cp == None):
	      print("-------------------------------------------------------------")    
	      print("Se debe crear un Comite de Programa previamente (opcion [0]).")
	      print("-------------------------------------------------------------")
	      continue
	    
	    clei.cp.to_string()
	    
	    print
	    print("PRESIDENTE")
	    print("----------")
	    print
	    
	    nombre = raw_input("Nombre: ")
	    usuario = None
	    miembros = clei.cp.get_miembros()
	    presidente = clei.cp.get_presidente()
	    
	    x = 0
	    while (x < len(miembros)) and (usuario == None):
	      if (miembros[x].nombre == nombre):
		usuario = miembros[x]
	      x += 1
	      
	    if (usuario == None):
	      print("--------------------------------------------------")    
	      print("El Miembro CP con nombre " + nombre + " no existe.")
	      print("---------------------------------------------------")
	      print
	    
	      ans = raw_input("Desea inscribirlo? (S/N) ")
	      if ans in ["n", "N"]:
		continue
	      
	      usuario = Miembro_CP()
	      clei.cp.agregar_miembro(presidente)
	      clei.agregar_inscrito(usuario)
	    
	    else:
	      index_usuario = clei.cp.get_miembros().index(usuario)
	      clei.cp.miembros[index_usuario] = presidente
	      
	    clei.cp.agregar_presidente(usuario)
	    
	    os.system('clear')
	    clei.cp.toString()

	    #print("Experticias: ")
	    #print(clei.getTopicos())

	    #experticias = []

	    #for i in range(0,3):
	      #exp = input()
	      #experticias.append(clei.topicos[exp])
	      
	    #print(experticias)  
	    #clei.cp.presidente.setExperticias(experticias)

	  elif (ans == "2"):   
	    if (clei.cp == None):
	      print("-------------------------------------------------------------")    
	      print("Se debe crear un Comite de Programa previamente (opcion [0]).")
	      print("-------------------------------------------------------------")
	      continue

	    print
	    print("MIEMBROS")
	    print("--------")
	    print

	    clei.cp.agregar_miembros()
	    
	    for x in range(len(miembros)):
	      clei.agregar_inscrito(miembros[x])
	    
	    os.system('clear')
	    
	    clei.cp.to_string()
	    
	  elif (ans == "3"):   
	    if (clei.cp == None):
	      print("-------------------------------------------------------------")    
	      print("Se debe crear un Comite de Programa previamente (opcion [0]).")
	      print("-------------------------------------------------------------")
	      continue
	    
	    clei.cp.to_string()
	    
	  elif (ans == "10"):
	    volver = True
	    
      elif (ans == "1"):
	if (clei.cp == None):
	  print("-------------------------------------------------------------")    
	  print("Se debe crear un Comite de Programa previamente (opcion [0]).")
	  print("-------------------------------------------------------------")
	  continue
	
	miembros = clei.cp.get_miembros()
	if (len(miembros) < 3):
	  print("-------------------------------------------------------------------------------")    
	  print("Para llamar a presentar articulos deben haber al menos 3 Miembros CP inscritos.")
	  print("-------------------------------------------------------------------------------")
	else:
	  print
	  ans = raw_input("Desea llamar a la presentacion de articulos? (S/N) ")
	  if ans not in ["n", "N"]:
	    clei.llamar_presArticulos();
	    os.system('clear')
	    
      elif (ans == "2"):
	print
	ans = raw_input("Desea finalizar la presentacion de articulos? (S/N) ")
	if ans not in ["n", "N"]:
	  clei.fin_pres_articulos()
	  os.system('clear')
	  
      elif (ans == "3"):
	print
	print "ARTICULOS RECIBIDOS"
	print "-------------------"
	
	print_articulos(clei.get_articulos())
	    
      elif (ans == "4") or (ans == "5") or (ans == "6"):
	pres_articulos = clei.get_pres_articulos()
	if (pres_articulos):
	  print
	  print("-------------------------------------------------------------------------------------")    
	  print("La lista no puede visualizarse mientras el proceso de envio de articulos este activo.")
	  print("-------------------------------------------------------------------------------------")    
	  print
	else:
	  if (ans == "4"):
	    print
	    print "ARTICULOS ACEPTABLES"
	    print "--------------------"
	    
	    print_articulos(clei.get_aceptables())
	    
	  elif (ans == "5"):
	    print
	    print "ARTICULOS ACEPTADOS"
	    print "-------------------"

	    print_articulos(clei.get_aceptados())
	    
	  elif (ans == "6"):
	    print
	    print "ARTICULOS EMPATADOS"
	    print "-------------------"
	    
	    print_articulos(clei.get_empatados())
	    
      elif (ans == "7"):
	espacio = Espacio()
	clei.agregar_espacio(espacio)
	
      elif (ans == "8"):
	evento = Evento()
	clei.agregar_evento(evento)
	print
	print ("Lugar: ")
	print("Ingrese Id del lugar a asignar: ")
	print
	lugar = raw_input(">> ")
	evento.set_lugar(lugar,clei.get_espacios)
	print
	
      elif (ans == "9"):
	programacion = Programacion()
	programacion.set_eventos(clei.get_eventos())
	programacion.generar_programacion()

      elif (ans == "10"):
	volver = True
	  
  elif (ans == "1"):

      print
      print("INSCRITO")
      print("--------")
      print
      
      nombre = raw_input("Nombre: ")
      usuario = None
      
      inscritos = clei.get_inscritos()
      
      x = 0
      while (x < len(inscritos)) and (usuario == None):
	if (inscritos[x].nombre == nombre):
	  usuario = inscritos[x]
	x += 1
      
      if (usuario == None):
	print
	print("------------------------------------")
	print("El usuario " + nombre + " no existe.")
	print("------------------------------------")
	print
	ans = raw_input("Desea inscribirse? (S/N) ")
	print
	if ans in ["n", "N"]:
	  os.system('clear')
	  continue
	
	usuario = Inscrito()
	
	#usuario = Inscrito(nombre)
	clei.agregar_inscrito(usuario)
	
	os.system('clear')
	      
      participacion = usuario.get_participacion()
      
      if (len(participacion) == 0):
	continue
      
      elif (len(participacion) == 1):
	part_seleccionada = participacion[0]
	
      else:
	print
	print("PARTICIPACION")
	print("-------------")
    
	usuario.print_participacion()
	ans = raw_input(">> ")
	while not (ans.isdigit()):
	  ans = raw_input(">> ")
	
	ans = int(ans)
	part_seleccionada = participacion[ans]
	
	os.system('clear')
	
      if (part_seleccionada == "Autor"):
	
	atras = False
	while not(atras):
	  print
	  print("AUTOR")
	  print("-----")
	  print
	  
	  if (clei.get_pres_articulos()):
	    print("[0] Crear Articulo")
	  else:
	    print("-----------------------------------------")    
	    print("CLEI no ha llamado a presentar articulos.") 
	    print("-----------------------------------------")
	    
	  print
	  print("[1] Agregar Participacion")
	  print
	  print("[10] Volver")
	  print
	  
	  ans = raw_input(">> ")
	  os.system('clear')

	  if (ans == "0"):
	    print
	    print("ARTICULO")
	    print("--------")
	    print   
	    
	    articulo = Articulo()
	    
	    print("Topico principal: ")
	    topico_principal = set_topicos(clei.get_topicos())
	    
	    articulo.set_topico_principal(topico_principal)
	    
	    print
	    print("Topico principal: " + articulo.topico_principal[0])
	    print
	    
	    print("Topicos secundarios: ")
	    topicos = clei.get_topicos()
	    #topicos.remove(topico_principal[0])
	    topicos_secundarios = set_topicos(topicos)
	    
	    articulo.set_topicos_secundarios(topicos_secundarios)
	    
	    print
	    print("Topicos secundarios: ")
	    printTopicos(articulo.topicos_secundarios)
	    
	    os.system('clear')
	    
	    existe_articulo = clei.encontrar_articulo(articulo)
	    
	    # Verificar que el articulo no este repetido.    
	    if (existe_articulo):
	      titulo = articulo.getTitulo()
	      print("--------------------------------------------------------")    
	      print("El articulo de titulo " + titulo + " ya esta registrado.")
	      print("--------------------------------------------------------")
	      
	      continue
	      
	    articulo.setNum_evaluadores(3)
	    clei.articulos.append(articulo)
	    clei.cp.miembros[0].articulos.append(articulo.getTitulo())
	    clei.cp.miembros[1].articulos.append(articulo.getTitulo())
	    clei.cp.miembros[2].articulos.append(articulo.getTitulo())	    
	    
	    print
	    print("Lista de Articulos")
	    print("------------------")
	    print(printArticulos(clei.getArticulos()))
	 
	  elif (ans == "1"):
	    
	    print
	    print("PARTICIPACION")
	    print("-------------")
	    print
	    print("[0] Autor")
	    print
	    print("[10] Volver")
	    print
	    
	    ans = raw_input(">> ")
	    while not (ans.isdigit()):
	      ans = raw_input(">> ")
	      
	    os.system('clear')
	      
	    ans = int(ans)
	    
	    if (ans == 0):
	      usuario.agregarParticipacion("Autor")
	    elif (ans == 10):
	      continue
	    
	  elif (ans == "10"):
	    atras = True
	    
      elif (part_seleccionada == "Miembro CP"):

	atras = False
	while not(atras):
	  print
	  print("MIEMBRO CP")
	  print("----------")
	  print
	  print("[0] Evaluar Articulo")
	  print      
	  print("[10] Volver")
	  print
	  
	  ans = raw_input(">> ")
	  os.system('clear')

	  if (ans == "0"):
	    articulos = usuario.getArticulos()
	    if (len(usuario.getArticulos()) == 0):
	      print("-------------------------------")    
	      print("No tiene articulos por evaluar.")
	      print("-------------------------------")    
	      continue

	    print
	    print("Lista de Articulos")
	    print("------------------")
	    print(usuario.printArticulos())
	    print

	    # Evaluar articulo
	    ans = raw_input(">> ")
	    while not (ans.isdigit()):
	      ans = raw_input(">> ")
	      
	    ans = int(ans)
	    
	    articulos_usuario = usuario.getArticulos()
	    titulo = articulos_usuario[ans]    
	    
	    fin = False
	    while not fin:
	      print("Puntuacion: [1-5] ")
	      puntos = raw_input(">> ")
	      while not (puntos.isdigit()):
		puntos = raw_input(">> ")
	      
	      puntos = int(puntos)
	      
	      if (puntos < 1) or (puntos > 5):
		print("La puntuacion debe estar entre 1 y 5.")
		continue
	      else: 
		print'%s %d %s' % ("la puntuacion dada fue ", puntos, ".")
		resp = raw_input("Es correcto? (S/N) ")
		fin = ans not in ["n", "N"]
  
	    clei.evaluar(titulo, puntos)
	    printArticulos(clei.getArticulos())
	    
	    usuario.removerArticulo(articulos_usuario[ans])
	    
	    evaluarPromedio(clei, titulo)
	  
	  elif (ans == "10"):
	    atras = True
    
  elif (ans == "10"):
    salir = True
