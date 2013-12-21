#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3
# main.py
# Programa principal
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
from ctypes import *
import os

from clases.Articulo import *
from clases.Conferencia import *
from clases.Cp import *
from clases.Espacio import *
from clases.Evaluacion import *
from clases.Evento import *
from clases.Inscrito import *
from clases.MiembroCp import *

# ------------------------------------------------------------
#		Funciones y Procedimientos
# ------------------------------------------------------------        

##
# print_articulos
# Impresion de una lista de articulos.
#
# Entrada: Lista de tipo Articulo.
##
def print_articulos(lista):
  if not (len(lista) == 0):
    print
    for x in range(len(lista)):
      print '%s %d %s %s' % ("[", x, "] Titulo ", lista[x].get_titulo())
      print '%s %d' % ("	Puntuacion: ", lista[x].get_puntuacion())
      print '%s %f' % ("	Promedio: ", lista[x].get_promedio())
      print '%s %d' % ("	Evaluaciones: ", lista[x].get_num_evaluaciones())
      print '%s %d' % ("	Evaluadores: ", lista[x].get_num_evaluadores())
      print '%s %s' % ("        Pais: ", lista[x].get_pais())

 #     print ("        Estado final: ")
      estado_final = lista[x].get_estado_final()
      if (estado_final == 0):
        print("        Aun sin definir.")
      elif (estado_final == 1):
        print("        ACEPTADO")
      elif (estado_final == 2):
        print("        ACEPTADO [Especial]")
      elif (estado_final == 3):
        print("        RECHAZADO [Falta de cupo]")  
      elif (estado_final == 4):
        print("        RECHAZADO [Promedio insuficiente]")
      else:
        print("        No definido.")

      print  
    print
  else:
    print
    print("-------------------------------")    
    print("La lista no contiene articulos.")
    print("-------------------------------")    
    print

##
# print_topicos
# Impresion de una lista de topicos.
#
# Entrada: Lista de tipo Topico.
##
def print_topicos(topicos):
  for x in range(len(topicos)):
    print '%s%d%s' % ("[", x, "] " + topicos[x])
    print     
    
##
# evaluar_promedio
# Clasificacion de un articulo segun la evaluacion de su promedio obtenido.
#
# Entrada: Conferencia, titulo de un Articulo.
##
#def evaluar_promedio(conf, titulo):
#  articulos = conf.get_articulos()
#  x = -1
#  fin = False

#  while (x < len(articulos)) and not fin:
#    x += 1
#    fin = (articulos[x].get_titulo() == titulo)
 
##  num_evaluadores = articulos[x].get_num_evaluadores()
#  num_evaluaciones = articulos[x].get_num_evaluaciones()
#  promedio = articulos[x].get_promedio()
#  max_articulos = conf.get_max_articulos()
 
#  if num_evaluaciones == num_evaluadores:
#    if not (promedio <= 2):
#      agregar_articulo(conf.get_aceptables(), conf.get_articulo(x))
    #else:
      # Rechazar articulo

##
# agregar_articulo
# Agrega un articulo a una lista dada.
#
# Entrada: Lista, Articulo.
##
#def agregar_articulo(lista, articulo):
#  lista.append(articulo)
   
def set_topicos(topicos):
  print
  print_topicos(topicos)
  
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

clei.set_max_articulos(3)

# Seccion de pruebas.
#articulo0 = Articulo()
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
#
#articulo3 = Articulo()
#articulo3.promedio = 3.2
#articulo3.num_evaluaciones = 3
#articulo3.num_evaluadores = 3
#
#articulo4 = Articulo()
#articulo4.promedio = 3.1
#articulo4.num_evaluaciones = 3
#articulo4.num_evaluadores = 3
#
#articulo5 = Articulo()
#articulo5.promedio = 3.1
#articulo5.num_evaluaciones = 3
#articulo5.num_evaluadores = 3
#
#articulo6 = Articulo()
#articulo6.promedio = 2
#articulo6.num_evaluaciones = 3
#articulo6.num_evaluadores = 3
#

articulo7 = Articulo()
articulo7.promedio = 4
articulo7.num_evaluaciones = 3
articulo7.num_evaluadores = 3

articulo8 = Articulo()
articulo8.promedio = 3
articulo8.num_evaluaciones = 3
articulo8.num_evaluadores = 3

articulo9 = Articulo()
articulo9.promedio = 3
articulo9.num_evaluaciones = 3
articulo9.num_evaluadores = 3

articulo10 = Articulo()
articulo10.promedio = 3
articulo10.num_evaluaciones = 3
articulo10.num_evaluadores = 3

#clei.articulos.append(articulo0)
#clei.articulos.append(articulo1)
#clei.articulos.append(articulo2)
#clei.articulos.append(articulo3)
#clei.articulos.append(articulo4)
#clei.articulos.append(articulo5)
#clei.articulos.append(articulo6)
clei.articulos.append(articulo7)
clei.articulos.append(articulo8)
clei.articulos.append(articulo9)
clei.articulos.append(articulo10)

print "ARTICULOS RECIBIDOS"
print "-------------------"
print
print_articulos(clei.articulos)

clei.armar_listas()

#clei.evaluar_promedio(articulo0.titulo)
#clei.evaluar_promedio(articulo1.titulo)
#clei.evaluar_promedio(articulo2.titulo)
#clei.evaluar_promedio(articulo3.titulo)
#clei.evaluar_promedio(articulo4.titulo)
#clei.evaluar_promedio(articulo5.titulo)
#clei.evaluar_promedio(articulo6.titulo)

print "ARTICULOS ACEPTABLES"
print "-------------------"
print
print_articulos(clei.aceptables)

#clei.calcular_aceptados()

print "ARTICULOS ACEPTADOS"
print "-------------------"
print
print_articulos(clei.aceptados)
print

print "ARTICULOS EMPATADOS"
print "-------------------"
print
print_articulos(clei.empatados)
print

#print "ARTICULOS RECHAZADOS"
#print "--------------------"
#print
#print_articulos(clei.rechazados)
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
  
  if ans == "0":
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
      print("[7] Lista de Articulos Rechazados")
      print
      print("[8] Registrar un espacio")
      print
      print("[9] Registrar un evento")
      print
      print("[10] Volver")
      print
      
      ans = raw_input(">> ")
      os.system('clear')

      if ans == "0":
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
	  
	  if ans == "0":
	    clei.cp = Cp()
	    
	    print
	    print("PRESIDENTE")
	    print("----------")
	    print
	    
	    presidente = MiembroCp()
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
	    
	  elif ans == "1":
	    if clei.cp == None:
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
	      if miembros[x].nombre == nombre:
		usuario = miembros[x]
	      x += 1
	      
	    if usuario == None:
	      print("--------------------------------------------------")    
	      print("El Miembro CP con nombre " + nombre + " no existe.")
	      print("---------------------------------------------------")
	      print
	    
	      ans = raw_input("Desea inscribirlo? (S/N) ")
	      if ans in ["n", "N"]:
		continue
	      
	      usuario = MiembroCp()
	      clei.cp.agregar_miembro(presidente)
	      clei.agregar_inscrito(usuario)
	    
	    else:
	      index_usuario = clei.cp.get_miembros().index(usuario)
	      clei.cp.miembros[index_usuario] = presidente
	      
	    clei.cp.agregar_presidente(usuario)
	    
	    os.system('clear')
	    clei.cp.to_string()

	    #print("Experticias: ")
	    #print(clei.getTopicos())

	    #experticias = []

	    #for i in range(0,3):
	      #exp = input()
	      #experticias.append(clei.topicos[exp])
	      
	    #print(experticias)  
	    #clei.cp.presidente.setExperticias(experticias)

	  elif ans == "2":   
	    if clei.cp == None:
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
	    
	  elif ans == "3":   
	    if clei.cp == None:
	      print("-------------------------------------------------------------")    
	      print("Se debe crear un Comite de Programa previamente (opcion [0]).")
	      print("-------------------------------------------------------------")
	      continue
	    
	    clei.cp.to_string()
	    
	  elif ans == "10":
	    volver = True
	    
      elif ans == "1":
	if clei.cp == None:
	  print("-------------------------------------------------------------")    
	  print("Se debe crear un Comite de Programa previamente (opcion [0]).")
	  print("-------------------------------------------------------------")
	  continue
	
	miembros = clei.cp.get_miembros()
	if len(miembros) < 3:
	  print("-------------------------------------------------------------------------------")    
	  print("Para llamar a presentar articulos deben haber al menos 3 Miembros CP inscritos.")
	  print("-------------------------------------------------------------------------------")
	else:
	  print
	  ans = raw_input("Desea llamar a la presentacion de articulos? (S/N) ")
	  if ans not in ["n", "N"]:
	    clei.llamar_pres_articulos();
	    os.system('clear')
	    
      elif ans == "2":
	print
	ans = raw_input("Desea finalizar la presentacion de articulos? (S/N) ")
	if ans not in ["n", "N"]:
	  clei.fin_pres_articulos()

          # Finalizado el periodo de presentacion de articulos, se evaluan los
          # promedios y se arman las listas de Aceptables, Aceptados y Rechazados.
          clei.armar_listas()
	  os.system('clear')
	  
      elif ans == "3":
	print
	print "ARTICULOS RECIBIDOS"
	print "-------------------"
	
	print_articulos(clei.get_articulos())

      elif ans in ["4", "5", "6", "7"]:
	pres_articulos = clei.get_pres_articulos()
	if pres_articulos:
	  print
	  print("-------------------------------------------------------------------------------------")    
	  print("La lista no puede visualizarse mientras el proceso de envio de articulos este activo.")
	  print("-------------------------------------------------------------------------------------")    
	  print
	else:
	  if ans == "4":
	    print
	    print "ARTICULOS ACEPTABLES"
	    print "--------------------"
	    print_articulos(clei.get_aceptables())
	    
	  elif ans == "5":
            print
            print("Seleccione la opcion para evaluar articulos:")
            print("-------------")
            print
            print("[0] Mejores promedios")
            print
            print("[1] Aceptados por pais")
            print
            print("[2] Promedios mayores a nota de corte")
            print
            new_ans = raw_input(">> ")
	    if new_ans == "0":
              eval = Evaluacion()
              listas = eval.calcular_aceptados_promedio(clei.aceptables,clei.get_max_articulos())
            if new_ans == "1":
              eval = Evaluacion(calcular_aceptados_pais)
              listas = eval.calcular_aceptados_promedio(eval,clei.aceptables,clei.get_max_articulos())
            if new_ans == "2":
              eval = Evaluacion(calcular_aceptados_nota)
              listas = eval.calcular_aceptados_promedio(eval,clei.aceptables,clei.get_max_articulos())
            print
	    print "ARTICULOS ACEPTADOS"
	    print "-------------------"
            clei.set_aceptados(listas[0])
	    print_articulos(clei.get_aceptados())
	    
	    print
	    print "ARTICULOS EMPATADOS"
	    print "-------------------"
            clei.set_empatados(listas[1])
	    print_articulos(clei.get_empatados())
      
     
          elif ans == "6":
	    print
	    print "ARTICULOS EMPATADOS"
	    print "-------------------"
	    
	    print_articulos(clei.get_empatados())

          elif ans == "7":
	    print
	    print "ARTICULOS RECHAZADOS"
	    print "--------------------"
	    
	    print_articulos(clei.get_rechazados())

      elif (ans == "8"):
        espacio = Espacio()
 	clei.agregar_espacio(espacio)
        print
        print "-------------------"
        print "Espacio registrado"
        print "-------------------"
	
      elif (ans == "9"):
        if (clei.get_cp() == None):
          print "Debe crearse un Comite de Programa previamente."
          continue

	evento = Evento()
        if (evento.get_tipo() in ["charla", "ponencia"]):
          evento.asignar_moderador(clei)
	clei.agregar_evento(evento)
        print
        print "-------------------"
        print "Evento registrado"
        print "-------------------"
           
      elif ans == "10":
	volver = True
	  
  elif ans == "1":

      print
      print("INSCRITO")
      print("--------")
      print
      
      correo = raw_input("Correo: ")
      usuario = None
      
      inscritos = clei.get_inscritos()
      
      # Revisar si el usuario ya existe chequeando por correo.
      x = 0
      while (x < len(inscritos)) and (usuario == None):
	if inscritos[x].get_correo() == correo:
	  usuario = inscritos[x]
	x += 1
      
      if usuario == None:
	print
	print("--------------------------------------------")
        print("No existe ningun usuario asociado al correo")
        print
        print(" \"" + correo + "\".")
	print("--------------------------------------------")
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
      
      if len(participacion) == 0:
	continue
      
      elif len(participacion) == 1:
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
	
      if part_seleccionada == "Autor":
	
	atras = False
	while not(atras):
	  print
	  print("AUTOR")
	  print("-----")
	  print
	  
	  if clei.get_pres_articulos():
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

	  if ans == "0":
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
	    print_topicos(articulo.topicos_secundarios)
	    
	    os.system('clear')
	    
	    existe_articulo = clei.encontrar_articulo(articulo)
	    
	    # Verificar que el articulo no este repetido.    
	    if existe_articulo:
	      titulo = articulo.get_titulo()
	      print("--------------------------------------------------------")    
	      print("El articulo de titulo " + titulo + " ya esta registrado.")
	      print("--------------------------------------------------------")
	      
	      continue
	      
	    articulo.set_num_evaluadores(3)
	    clei.articulos.append(articulo)
	    clei.cp.miembros[0].articulos.append(articulo.get_titulo())
	    clei.cp.miembros[1].articulos.append(articulo.get_titulo())
	    clei.cp.miembros[2].articulos.append(articulo.get_titulo())	    
	    
	    print
	    print("Lista de Articulos")
	    print("------------------")
	    print(print_articulos(clei.get_articulos()))
	 
	  elif ans == "1":
	    
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
	    
	    if ans == 0:
	      usuario.agregar_participacion("Autor")
	    elif ans == 10:
	      continue
	    
	  elif ans == "10":
	    atras = True
	    
      elif part_seleccionada == "Miembro CP":

	atras = False
	while not(atras):
	  print
	  print("MIEMBRO CP")
	  print("----------")
	  print
	  print("[0] Evaluar Articulo")
          print
          cp = clei.get_cp()
          presidente = cp.get_presidente()
          if (usuario.get_correo() == presidente.get_correo()):
            print("[1] Gestion de Articulos Empatados") 
	    print 
	  print("[10] Volver")
	  print
	  
	  ans = raw_input(">> ")
	  os.system('clear')

	  if ans == "0":
	    articulos = usuario.get_articulos()
	    if len(usuario.get_articulos()) == 0:
	      print("-------------------------------")    
	      print("No tiene articulos por evaluar.")
	      print("-------------------------------")    
	      continue

	    print
	    print("Lista de Articulos")
	    print("------------------")
	    print(usuario.print_articulos())
	    print

	    # Evaluar articulo
            articulos_usuario = usuario.get_articulos()

            fin = False
	    while not fin:
	      ans = raw_input(">> ")
              if ans.isdigit():
                ans = int(ans)
                fin = (ans < len(articulos_usuario) and (ans >= 0))
	    
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
	    print_articulos(clei.get_articulos())
	    
	    usuario.remover_articulo(articulos_usuario[ans])
	    
	    #clei.evaluar_promedio(titulo)
	  
          elif ans == "1":
	    if clei.get_pres_articulos():
	      print
              print("-------------------------------------------------------------------------------------")    
	      print("La gestion no puede realizarse mientras el proceso de envio de articulos este activo.")
	      print("-------------------------------------------------------------------------------------")    
	      print
              continue

            os.system('clear')
            print "aceptados"
            print_articulos(clei.get_aceptados())
            print "empatados"
            print_articulos(clei.get_empatados())
            print "rechazados"
            print_articulos(clei.get_rechazados())
            if not (len(clei.get_empatados()) <= 0):
              usuario.gestionar_empatados(clei)

            print "aceptados actualizada"
            print_articulos(clei.get_aceptados())
            print "empatados actualizada"
            print_articulos(clei.get_empatados())
            print "rechazados actualizada"
            print_articulos(clei.get_rechazados())

	  elif ans == "10":
	    atras = True
    
  elif ans == "10":
    salir = True
                  
