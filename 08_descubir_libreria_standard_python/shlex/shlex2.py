import shlex 
 
def interprete(l�nea): 
   s = shlex.shlex(l�nea, posix=False, punctuation_chars=False) 
   s.whitespace_split = False 
   cmd = arg = tiempo = "" 
   cmd = s.get_token() 
   if cmd == "create": 
       arg = s.get_token() 
       tiempo = s.get_token() 
   elif cmd == "list": 
       pass 
   elif cmd == "kill": 
       arg = s.get_token() 
   else: 
       cmd = "Error ..." 
   print("cmd=%s arg=%s tiempo=%s" % (cmd, arg, tiempo)) 
 
 
while True: 
   linea = input("Escriba una cadena en el int�rprete:") 
   interprete(linea)
