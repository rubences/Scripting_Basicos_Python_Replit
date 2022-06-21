html_doc = """\ 
       <html> 
       <head> 
       <title> Mi P�gina Web </title> 
       </head> 
       <body> 
       <h1> Esta es una p�gina WEB </h1> 
       <p> A continuaci�n se muestra un peque�o texto a encontrar </p> 
       <ul> 
       <li> <a href="http://example.com/enlace1">Enlace 1</a> </li> 
       <li> <a href="http://example.com/enlace2">Enlace 2</a> </li> 
       <li> <a href="http://example.com/enlace3">Enlace 3</a> </li> 
       <li> <a href="http://example.com/enlace4">Enlace 4</a> </li> 
       </ul> 
       <table class='mi_class'> 
           <thead> 
               <td> Sistema </td> 
               <td> Gobierno </td> 
               <td> Nivel tecnol�gico </td> 
               <td> Poblaci�n </td> 
           </thead> 
           <tbody> 
           <tr>     
               <td>Lave</td> 
               <td>Dictatura</td> 
               <td>Agricultores ricos</td> 
               <td>2,5 M</td> 
           </tr> 
           <tr>     
               <td>Teaatis</td> 
               <td>Feodal</td> 
               <td>Agricultores normales </td> 
               <td>1,6 M</td> 
           </tr> 
           <tr>     
               <td>Riinus</td> 
               <td>Comuistas</td> 
               <td>Industria media </td> 
               <td>4,2 M</td> 
           </tr> 
           <tr>     
               <td>Diurezza</td> 
               <td>Gobierno m�ltiple</td> 
               <td>Industriales Ricos</td> 
               <td>8,5 M</td> 
           </tr> 
           </tbody> 
 
       </table> 
       </body> 
       </html> 
""" 
 
from bs4 import BeautifulSoup 
import pprint 
 
pp = pprint.PrettyPrinter(indent=4) 
 
soup = BeautifulSoup(html_doc, 'lxml') 
 
print("== T�tulo de la p�gina ==") 
print( soup.title.text ) 
 
print("== Extracci�n de los enlaces ==") 
for l in soup.find_all('a'): 
   print(l.text, l.get('href')) 
 
## Extracci�n de la tabla 
data = [] 
table = soup.find('table', attrs={ 'class':'mi_class'}) 
tbody = table.find('tbody') 
 
for row in tbody.find_all('tr'): 
   cols = row.find_all('td') 
   elt = [ x.text for x in cols ] 
   data.append( elt ) 
 
print("== Extracci�n de la tabla ==") 
print(pp.pprint(data))
