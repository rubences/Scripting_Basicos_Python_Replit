from datetime import * 
from dateutil.relativedelta import * 
 
## Hoy
today = datetime.now() 
 
# Fecha de salida de la primera versi�n de python 
python_v1 = datetime(1991, 2, 20, 12, 00, 00) 
 
## C�lculo del n�mero de d�as desde una fecha con datetime 
print( 'datetime today - python_v1: ', today - python_v1) 
 
# c�lculo con dateutil  
print( 'dateutil today - python_v1: ', relativedelta(today, python_v1)) 
 
# dateutil permite a�adir meses y a�os 
print("relative delta: a�de de 1 a�o + 1 mes: ", 
today+relativedelta(years=+1, months=+1)) 
 
# y tambi�n resta 
print("relative delta: resta 1 a�o: ", today+relativedelta(years=-1))
