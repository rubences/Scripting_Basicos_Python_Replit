
def f1( arg1 ): 
   arg1.append("UNO") 
   return arg1 
 
a = [1,2,3,4] 
b = f1(a[:])    # a[:] es una copia de la lista 
               # o a.copy() 
print("Despu�s de la funci�n a = ", a) 
print("Despu�s de la funci�n b = ", b)
