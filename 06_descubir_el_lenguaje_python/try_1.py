
OK = False 
 
while not OK: 
   try: 
       n = int(input("Escriba un n�mero: ")) 
       OK = True 
   except TypeError, ValueError: 
       print(" Error de tipo ... ") 
   else: 
       print("Cl�usula Else") 
   finally: 
       print("Cl�sula Finally") 
 
print("Salida del bucle")
