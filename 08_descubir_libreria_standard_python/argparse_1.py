import argparse 
 
def mi_programa(opciones): 
   print("Mi programa ") 
   print("Opciones: %s " % opciones ) 
 
if __name__ == '__main__': 
   ## gesti�n de los argumentos 
   parser = argparse.ArgumentParser() 
   parser.add_argument('-f', '--archivo', help='Nombre de archivo' ) 
   parser.add_argument('-v', '--verbose', help='Modo verboso', 
                                action='store_true' ) 
 
   opciones = parser.parse_args() 
 
   # ejecuci�n de mi funci�n pasando las opciones 
   # como argumento 
   mi_programa(opciones)
