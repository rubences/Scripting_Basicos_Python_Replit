
archivo = "data.txt"           # el nombre del archivo 
 
fd = open(archivo)             # apertura 
 
for l in fd:                   # lectura l�nea a l�nea 
   print("l=%s" % l, end='')   # utilizaci�n de los datos
 
fd.close()                     # cierre
