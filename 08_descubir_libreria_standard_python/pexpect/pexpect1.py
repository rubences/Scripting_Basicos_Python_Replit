import pexpect 
servidor = "speedtest.tele2.net" 
username = "anonymous" 
password = "root@ejemplo.com" 
 
child = pexpect.spawn ('ftp %s' % servidor)# ejecuci�n del binario 
child.expect ('Name .*: ')                  # espera 
child.sendline (username)                   # env�a 
child.expect ('Password:')                  # espera 
child.sendline (password)                   # env�a 
child.expect ('ftp> ')                      # etc ... 
child.sendline ('ls -l') 
child.expect ('ftp> ') 
print(child.before)   # Muestra el resultado 
child.sendline ('sale') 


