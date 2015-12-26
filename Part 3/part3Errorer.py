ECB = ''
CBC = ''
CFB = ''
OFB = ''

with open('cipherECB.enc', 'rb') as f, \
     open('cipherCBC.enc', 'rb') as g, \
     open('cipherCFB.enc', 'rb') as h, \
     open('cipherOFB.enc', 'rb') as i:
   count = 0
   # ECB
   # EOF has not been reached
   while 1:
      count += 1
      # Read a byte
      byte_s = f.read(1)
      
      # EOF, break
      if not byte_s:
         break

      if not ECB:
         ECB = byte_s
      else:
         if count != 19:
            # Append character to ECB
            ECB += byte_s    
         else:
            ECB += b'\x00'
   count = 0
   # CBC
   while 1:
      count += 1
      # Read a byte
      byte_s = g.read(1)
      
      # EOF, break
      if not byte_s:
         break   
   
      if not CBC:
         CBC = byte_s
      else:
         if count != 19:
            # Append character to ECB
            CBC += byte_s    
         else:
            CBC += b'\x00'  
   count = 0
   # CFB
   while 1:
      count += 1
      # Read a byte
      byte_s = h.read(1)
      
      # EOF, break
      if not byte_s:
         break   
   
      if not CFB:
         CFB = byte_s
      else:
         if count != 19:
            # Append character to ECB
            CFB += byte_s    
         else:
            CFB += b'\x00'   
   count = 0
   # OFB
   while 1:
      count += 1
      # Read a byte
      byte_s = i.read(1)
      
      # EOF, break
      if not byte_s:
         break   
      
      if not OFB:
         OFB = byte_s
      else:
         if count != 19:
            # Append character to ECB
            OFB += byte_s    
         else:
            OFB += b'\x00'         
         

with open('cipherECBerror.enc', 'wb') as f, \
     open('cipherCBCerror.enc', 'wb') as g, \
     open('cipherCFBerror.enc', 'wb') as h, \
     open('cipherOFBerror.enc', 'wb') as i:
   
   # ECB
   f.write(ECB)
   # CBC
   g.write(CBC)
   # CFB
   h.write(CFB)
   # OFB
   i.write(OFB)