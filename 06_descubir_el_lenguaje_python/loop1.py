
print(" Bucle con break ")
for x in range(0,10):
    print(x)
    if x == 5:
        break

print(" Bucle con continue ") 
for x in range(0,10): 
    if x == 5: 
       print(" Aqu� continua") 
       continue  
    print(x)         #esta l�nea no se ejecuta si x vale 5 
