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
class Evaluacion:
    def __init__(self, func=None):
      if func:
        self.calcular_aceptados_promedio = func
    
    def calcular_aceptados_promedio(self,aceptables,max_articulos):
        aceptados = []
        empatados = []
      
        if len(aceptables) > max_articulos:
          promedio_min = aceptables[max_articulos - 1].get_promedio()
      
          if aceptables[max_articulos].get_promedio() == promedio_min:      
            x = max_articulos - 2
            while (x >= 0) and (aceptables[x].get_promedio() == promedio_min):
                x -= 1
	    
                y = x + 1
            while (y < len(aceptables)) and (aceptables[y].get_promedio() == promedio_min):
                y += 1
	    
            for i in range(x + 1):
                aceptados.append(aceptables[i])
	    
            for i in range(x + 1, y):
                empatados.append(aceptables[i])
          else:
            for x in range(max_articulos):
                aceptados.append(aceptables[x])
 
        else:
            for x in range(len(aceptables)):
                aceptados.append(aceptables[x])
        
        return (aceptados,empatados)
    
def calcular_aceptados_pais(self,aceptables,max_articulos):
    aceptados = []
    empatados = []
    diccionario = {}
    dicc_pais = {}
    
    for x in range(len(aceptables)):
        pais = aceptables[x].get_pais()
        
        if diccionario.has_key(pais):
            lista = diccionario[pais]
            lista_pais = dicc_pais[pais]
            cont = lista.pop(0)
            cont += 1
            lista.insert(0,cont)
            lista_pais.append(aceptables[x])
	else:
            lista = []
            lista_pais = []
            cont = 1
            lista.append(cont)
            lista_pais.append(aceptables[x])
            
	diccionario[pais] = lista
        dicc_pais[pais] = lista_pais

    for x in dicc_pais.keys():
        lista_pais = dicc_pais[x]
        lista_pais.sort(key=lambda x: x.get_promedio(), reverse = True)
        dicc_pais[x] = lista_pais
    
    print("Numero de articulos aceptados por pais: ")
    num = int(raw_input(">> "))
    
    while num < 1 and num >= max_articulos:
        print("No es posible realizar la operacion. Seleccione otro numero: ")
        num = int(raw_input(">> "))
    
    total_aceptados = 0
    num_aceptables = len(aceptables)
    
    while num_aceptables > 0 and total_aceptados < max_articulos and num > 0:
        num -= 1
        
        for x in dicc_pais.keys():
            lista = diccionario[x]
            lista_pais = dicc_pais[x]
        
            cont = lista.pop(0)
        
            if cont > 0 and total_aceptados < max_articulos:
                articulo = lista_pais.pop(0)
                aceptados.append(articulo) 
                total_aceptados += 1
                cont -= 1
                num_aceptables -= 1
                dicc_pais[x] = lista_pais
                
            lista.insert(0,cont)
            diccionario[x] = lista
             
    
    if num_aceptables > 0 and total_aceptados < max_articulos:
        aceptables.sort(key=lambda x: x.get_promedio(), reverse = True)
        
        for x in range(len(aceptables)):
            y = 0
            fue_aceptado = True
            
            while (y < len(aceptados)) and not (aceptables[x].get_titulo() == aceptados[y].get_titulo()):
                y += 1
	
                if y == len(aceptados):
                    fue_aceptado = False
                    
            if not fue_aceptado and total_aceptados < max_articulos:
                aceptados.append(aceptables[x])
                total_aceptados += 1
                
        
    return(aceptados,empatados)
        
    
def calcular_aceptados_nota(self,aceptables,max_articulos):
    aceptados = []
    empatados = []

    fin = False
    while not fin:
        print("Nota de corte: [1-5] ")
        nota = float(raw_input(">> "))
	      
	if (nota < 1.00) or (nota > 5.00):
            print("La nota de corte debe estar entre 1 y 5.")
            continue
	else: 
            print'%s %f' % ("La nota de corte es ", round(nota,2))
            resp = raw_input("Es correcto? (S/N) ")
            fin = resp not in ["n", "N"]

    if len(aceptables) > max_articulos:
        cont = 0
        for x in range(len(aceptables)):
            if cont < max_articulos and aceptables[x].get_promedio() >= nota:
                aceptados.append(aceptables[x])
                cont += 1
    else:
        for x in range(len(aceptables)):
            if aceptables[x].get_promedio() >= nota:
                aceptados.append(aceptables[x])
            
    return (aceptados,empatados)
