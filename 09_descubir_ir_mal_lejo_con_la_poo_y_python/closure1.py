## F�brica de funci�n 
def func1(): 
   def s_func1(): 
       print(" S_func1 ") 
   return s_func1 
 
## Recupeamos una funci�n 
f = func1() 
 
## La utilizamos 
f() 
f()
