import telnetlib 
 
HOST = "localhost" 
PORT=2601 
user = 'zebra'    # la conexi�n solo pide una 
password = ''     # contrase�a 
 
tn = telnetlib.Telnet(HOST,PORT)               #conexi�n 
 
tn.read_until(b"Password: ")               # espera prompt 
tn.write(user.encode('ascii') + b"\n")     # env�o password 
 
tn.write(b"enable\n")                      # env�o comando 
tn.read_until(b"Password: ")               # esperar prompt 
tn.write(user.encode('ascii') + b"\n")     # env�o password 
tn.write(b"show startup-config\n")         # env�o comando 
tn.write(b"quit\n")                        # env�o comando 
 
print(tn.read_all().decode('ascii'))       # recupera al info
