def mi_deco(funci�n): 
   return funci�n 
 
@mi_deco 
def funcion1(): 
    print("Soy la funci�n 1 ") 
 
@mi_deco 
def funcion2(): 
    print("Soy la funci�n 2 ") 
 
@mi_deco 
def funcion3(): 
    print("Soy la funci�n 3 ") 
 
## Llamada a las funciones 
funcion1() 
funcion2() 
funcion3() 
funcion1()
