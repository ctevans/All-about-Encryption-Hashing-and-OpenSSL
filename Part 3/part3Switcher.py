import sys

try:
   # Read bytes into the array
   array = ''
   
   with open('ciphertext3', 'rb') as f:
      # EOF has not been reached
      while 1:
         # Read a byte
         byte_s = f.read(1)
         
         # EOF, break
         if not byte_s:
            break
         
         # Append character to array
         array += chr(ord(byte_s))
         
   student1 = array[:8]
   student2 = array[32:40]
   
   old = array
   array = student2 + array[8:]
   array = array[:32] + student1 + array[40:] 
   
   with open('switched', 'wb') as f:
      f.write(array)
      
except:
   print()
   
   