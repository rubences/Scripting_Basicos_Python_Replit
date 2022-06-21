import spur 
 
shell = spur.SshShell(hostname="<servidor o direcci�n IP>", \ 
                         username="<usuario>", \ 
                         password="<si es necesario>" 
              ) 
with shell: 
   result = shell.run(["echo", "-n", "hello"]) 
   print(result.output) # prints hello 
   result = shell.run(["ls", "-l"]) 
   print(result.output) 
