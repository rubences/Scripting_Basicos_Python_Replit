def gener(): 
   print(" Hola, empezamos ...    : Antes del primer yield") 
   yield(" Esta parte est� al inicio: 1er yield") 
   yield(" Esta al final del inicio: 2� yield") 
   yield(" Esta en la mitad: 3er yield") 
   yield(" Esta al inicio del final    : 4� yield") 
   yield(" Casi al final : 5� yield") 
   yield(" Todav�a falta un poco: 6� yield") 
   print(" The End                     : no hay m�s yield") 
 
for i in gener(): 
   print(i)
