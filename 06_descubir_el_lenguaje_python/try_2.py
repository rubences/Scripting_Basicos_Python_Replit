try: 
   raise NameError(" Mi Texto �")      # desencadenamiento 
except NameError as err: 
   print("Error de nombre: %s " % err )  # intercepci�n
   raise                                # propagaci�n
