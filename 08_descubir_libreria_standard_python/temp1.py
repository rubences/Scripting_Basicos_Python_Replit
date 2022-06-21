import tempfile 
 
data = [ 'l�nea 1\n', 'l�nea 2\n', 'l�nea 3\n' ] 
 
with tempfile.TemporaryFile(mode='w+') as fic: 
   fic.writelines( data )                     # escritura 
   fic.flush()                                # forzada 
   fic.seek(0)                                # rewind 
   print(fic.read())                          # lectura
