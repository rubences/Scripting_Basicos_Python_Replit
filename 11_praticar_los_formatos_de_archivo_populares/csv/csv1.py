import csv 
from fake_contact import fake_contact 
 
archivo = "contactos.csv" 
 
with open(archivo, 'w', newline='') as csvfile: 
   writer = csv.writer(csvfile, delimiter='\t', quotechar='"' ) 
 
   for x in range(0,5): 
       writer.writerow( fake_contact() )
