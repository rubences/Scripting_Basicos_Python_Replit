archivo = "data.txt" 
 
fd = open(archivo, "w")                     # apertura en 
                                            # modo escritura 
 
for n in range(1, 6): 
   f.write("L�nea No %s del archivo\n" % n)  # escritura 
 
f.close()                                   # cierre
