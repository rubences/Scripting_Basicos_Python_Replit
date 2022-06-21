import random   # importamos el m�dulo random 
                # para la generaci�n de n�mero aleatorios
 
## Crea un paquetee de 32 cartas
## una lista de 32 enteros del 1 al 32
paquete = [x for x in range(1, 32)] 
 
mezcla = []         # al inicio el resultado est� vac�o
 
 
print(paquete)        # mostramos al menos el paquete ordenado 
 
while paquete:                               # mientras que quede 
   mezcla.append(                            # a�adimos
           paquete.pop(                      # lo que eliminamos 
               paquete.index(                # a este �ndice 
                   random.choice(paquete)    # elegido al azar 
                   )                         #    en la lista 
               ) 
           ) 
 
print(mezcla)      # Mostramos el resultado mezclado
