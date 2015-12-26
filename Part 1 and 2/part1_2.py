import sys
import string

# Given a mapped byte and byte of the key unmap it
def unmapper(c, k):  
   for i in range(len(matrix_)):
      if matrix_[i][int(k, 2)] == int(c, 2):
         return i

# Given a byte of plaintext and key, encrypt it
def forward(p, k):  
   # Turn p and k into binary
   p = toBinary(p)
   k = toBinary(k)
   
   # Separate the higher and lower bits
   ph = p[:4]
   pl = p[4:]
   kh = k[:4]
   kl = k[4:]   

   # First mapping
   a = matrix_[int(ph,2)][int(kl,2)]
   b = matrix_[int(pl,2)][int(kh,2)]
   
   # Second mapping
   ch = matrix_[b][int(kl, 2)]
   cl = matrix_[a^b][int(kh, 2)]
   
   return toBinary(ch)[4:] + toBinary(cl)[4:]


# Given a byte of ciphertext and key, decrypt it 
def reverse(c, k):   
   # Turn c and k into binary
   c = toBinary(c)
   k = toBinary(k)
   
   # Separate the higher and lower bits
   ch = c[:4]
   cl = c[4:]
   kh = k[:4]
   kl = k[4:]   
   
   # First unmapping
   b = unmapper(ch, kl)
   a = unmapper(cl, kh)^b
   
   # Second unmapping
   ph = unmapper(toBinary(a), kl) 
   pl = unmapper(toBinary(b), kh)
   
   return toBinary(ph)[4:] + toBinary(pl)[4:]

# Turn a character or integer to its binary representation
def toBinary(x):
   # Turn characters into decimal representation before turning it into binary
   if type(x) == str:
      x = ord(x)
      
   return '{:08b}'.format(x)

# Decrypt the data
def decrypt(data, key):
   # Decrypt every character of data and append character to s
   s = ''
   
   for position in range(len(data)):
      s += chr(int((reverse(data[position], key[position%len(key)])), 2))
      
   return s

# Mapping
matrix_ = [[0x7, 0x5, 0x0, 0x4, 0x2, 0x3, 0xb, 0x6, 0xa, 0x8, 0x9, 0xd, 0xc, 0xf, 0xe, 0x1], 
     [0x3, 0x8, 0xd, 0xa, 0xc, 0xe, 0xf, 0xb, 0x7, 0x6, 0x4, 0x5, 0x1, 0x2, 0x0, 0x9], 
     [0x4, 0x0, 0x3, 0x1, 0xb, 0xa, 0x8, 0x5, 0x9, 0xd, 0xc, 0xe, 0xf, 0x6, 0x7, 0x2], 
     [0x9, 0xe, 0x7, 0xc, 0x6, 0x4, 0x5, 0xd, 0x1, 0x0, 0x2, 0x3, 0xb, 0x8, 0xa, 0xf], 
     [0x1, 0x3, 0xa, 0x2, 0x8, 0x9, 0xd, 0x0, 0xc, 0xe, 0xf, 0x7, 0x6, 0x5, 0x4, 0xb], 
     [0xe, 0x6, 0x5, 0x7, 0x1, 0x0, 0x2, 0xf, 0x3, 0xb, 0xa, 0x8, 0x9, 0xc, 0xd, 0x4], 
     [0x2, 0xa, 0x9, 0xb, 0xd, 0xc, 0xe, 0x3, 0xf, 0x7, 0x6, 0x4, 0x5, 0x0, 0x1, 0x8], 
     [0xd, 0xf, 0x6, 0xe, 0x4, 0x5, 0x1, 0xc, 0x0, 0x2, 0x3, 0xb, 0xa, 0x9, 0x8, 0x7], 
     [0xb, 0x9, 0xc, 0x8, 0xe, 0xf, 0x7, 0xa, 0x6, 0x4, 0x5, 0x1, 0x0, 0x3, 0x2, 0xd], 
     [0x0, 0xb, 0x8, 0x3, 0x9, 0xd, 0xc, 0x2, 0xe, 0xf, 0x7, 0x6, 0x4, 0x1, 0x5, 0xa], 
     [0x8, 0xc, 0xf, 0xd, 0x7, 0x6, 0x4, 0x9, 0x5, 0x1, 0x0, 0x2, 0x3, 0xa, 0xb, 0xe], 
     [0x5, 0x2, 0xb, 0x0, 0xa, 0x8, 0x9, 0x1, 0xd, 0xc, 0xe, 0xf, 0x7, 0x4, 0x6, 0x3], 
     [0x6, 0x1, 0x2, 0x5, 0x3, 0xb, 0xa, 0x4, 0x8, 0x9, 0xd, 0xc, 0xe, 0x7, 0xf, 0x0], 
     [0xc, 0x7, 0x4, 0xf, 0x5, 0x1, 0x0, 0xe, 0x2, 0x3, 0xb, 0xa, 0x8, 0xd, 0x9, 0x6], 
     [0xa, 0xd, 0xe, 0x9, 0xf, 0x7, 0x6, 0x8, 0x4, 0x5, 0x1, 0x0, 0x2, 0xb, 0x3, 0xc], 
     [0xf, 0x4, 0x1, 0x6, 0x0, 0x2, 0x3, 0x7, 0xb, 0xa, 0x8, 0x9, 0xd, 0xe, 0xc, 0x5]]

# Key can be lowercase, uppercase, digits or special characters
ords = [x for x in range(32, 127)]

if len(sys.argv) == 2 or len(sys.argv) == 4:
   try:
      # Read bytes into the array
      array = ''
      
      with open(sys.argv[1], 'rb') as f:
         # EOF has not been reached
         while 1:
            # Read a byte
            byte_s = f.read(1)
            
            # EOF, break
            if not byte_s:
               break
            
            # Append character to array
            array += chr(ord(byte_s))
            
   except:
      # Error opening file
      print("Unable to open %s"%(sys.argv[1]))   
      sys.exit(0)
   
   partial_text = ''
   mode = ''
   
   # Set up parameters if they are available
   if len(sys.argv) == 4:
      partial_text = sys.argv[3]
      mode = sys.argv[2]
            
      # Invalid mode
      if mode != '-d' and mode != '-p':
         print("Invalid mode")
         sys.exit(0)      
         
   # Decryption mode
   if mode == '-d':
      print(decrypt(array, sys.argv[3]))
      
   else:
      
      # Partial plaintext mode
      # Assume key is of the same length as partial plaintext
      # Create a list of possibilities for each character
      partial_key = [[y for y in ords] for x in range(len(partial_text))]
      
      if mode == '-p':         
         print("Partial plaintext: %s"%(partial_text))
         
         # Iterate through partial text characters
         for i in range(len(partial_text)):
            
            # Iterate through possible key characters
            for j in range(len(ords)):
               
               # Non-matching cipher, remove the character from current spot
               if chr(int(forward(partial_text[i], ords[j]), 2)) != array[i]:
                  partial_key[i][j] = ''      
         
         # Remove all the blanks
         partial_key = [[y for y in x if y != ''] for x in partial_key]
         
         # There was a spot with no possibilities
         if [] in partial_key:
            print('This partial plaintext is not possible with any key value')
            sys.exit(0)  
         # Possible, print possibilities in a readable form
         else:
            print("Possible partial key:")
            print([[chr(y) for y in x if y != ''] for x in partial_key])
            
         print()       
         
      # Find repetitions and maximum gap between the most frequent longest one
      occurences = {}
      max_keys = []
      max_gap = False
      key_length = False
      length = 2
      
      while True:
         # Upper length of repetition
         if length > 200:
            print("Repetition of 200 is good enough")
            break
         
         # Print how many bytes are combined together
         print("Number of bytes: %d bytes"%(length))   
         
         # Keep track of occurences and minimum gap for each block
         # and list of the blocks that have the minimal gap
         blocks = {}
         min_gaps = {}
         min_gap = len(array)
         i = 0
         while i + length < len(array):
            # Create current block
            s = array[i:i+length]
            
            if s not in blocks:
               blocks[s] = [i]  
            else:
               blocks[s] += [i]
               
               # Calculate gap between current occurence and previous occurence
               gap = i - blocks[s][len(blocks[s])-2]
                  
               # Current gap smaller than or equal to previously found gaps
               if gap <= min_gap:
                  # Scrictly smaller, previous list of minimal gap blocks is not useful
                  if gap < min_gap:
                     min_gap = gap
                     min_gaps = {}
                     
                  min_gaps[s] = gap                           
            
            i += 1        
         
         if min_gaps:
            # Repetitions were found, report the minimum gap and the keys associated with it
            print("Minimum gap size: %d bytes"%(min_gap*8))
            
            # Update maximum gap and the key length associated with it
            if not max_gap or min_gap >= max_gap:
               max_gap = gap 
               key_length = length
               
            # Find keys with most occurences
            max_occurence = 0
            max_keys = []
            for k in min_gaps:
               n = len(blocks[k])
               
               # Current block more frequent, previous list of blocks is not useful
               if n > max_occurence:
                  max_occurence = n
                  max_keys = [k]
                  
               # Current block is just as frequent, add it to the list
               elif n == max_occurence:
                  max_keys.append(k)
            
            # Print out the number of equally frequent keys and their number of occurences each
            print("Number of keys: %d"%(len(max_keys)))   
            print("Number of occurences each: %d"%(max_occurence))    
            
            # Add the occurences into the dictionary
            occurences = {}
            for k in max_keys:
               occurences[k] = blocks[k]
              
            length += 1
            
            print()
         else:
            # No repetitions were found, no longer need to keep going
            print("No repetitions")
            break
      
      print()
      
      # Output longest repition length and maximum gap size
      print("Longest repetition length: %d bytes"%(length - 1))
      print("Maximum gap between repetitions: %d bytes with %d length key"%(max_gap*8, key_length))
      
      print()
      
      # Find possible lengths that give proper cycles
      print("Possible key lengths: ")
      lengths = []
      
      # Key can't be longer than the longest cycle plus the size of repetition
      for n in range(2, max_gap*8 + key_length): 
         # Iterate through every max key
         for i in range(len(max_keys)):
            possible = True
            
            # First occurence
            start = occurences[max_keys[i]][0]
            end = start + key_length
            
            # Look at every byte of the repeitition
            for k in range(start, end+1):
               if possible:
                  # Iterate through the other occurences
                  for j in range(1 , len(occurences[max_keys[i]])):
                     # Make sure that the bytes will land on the same spot on the cycle (cause of repetition)
                     if (start+k)%n != (occurences[max_keys[i]][j]+k)%n:
                        possible = False
                        break       
               else: 
                  break
            
         # Cycles match, this is a possible key length
         if possible:
            lengths.append(n)

      print()
      
      print("Possibilities:")
      
      # Iterate through the possible lengths
      for length in range(len(lengths)):
         print("Length: %d"%(lengths[length]))
         
         # Create a list of possibilities for each character
         # First add result of partial_key, up to the length
         possibilities = [[x for x in partial_key[i]] for i in range(min(len(partial_key), lengths[length]))]
         
         # Fill in the rest of the length if necessary
         for i in range(len(partial_key), lengths[length]):
            possibilities.append([x for x in ords])   
         
         # Iterate through array
         i = 0
         possible = True  
         
         while i + lengths[length] < len(array):
            # Current length is still possible
            if possible:
               # Iterate through the spots
               for letter in range(lengths[length]):
                  # Iterate through the remaining possible key characters
                  for k in range(len(possibilities[letter])):   
                     # Decrypt using current key character
                     x = int(reverse(array[i+letter], possibilities[letter][k]), 2)
                     
                     # Result not a valid printable character, remove from possibilities
                     if x > 126 or (x < 32 and x != 9 and x != 10 and x != 13):
                        possibilities[letter][k] = ''
                  
                  # Remove blanks
                  possibilities[letter] = [x for x in possibilities[letter] if x != '']
                  
                  # No possibilites remaining for current spot, end the search for current length
                  if not possibilities[letter]:
                     possible = False
                     break
                  
               i += lengths[length]
            
            # Current length has a byte with no possibilities
            else:
               break
         
         if possible:
            # Convert possibilities to a readable form
            possibilities = [[chr(y) for y in possibilities[x] if y != '']  for x in range(lengths[length])]  
            print(possibilities)
         else:
            print('Not possible')
            
         print()         

else: 
   # Not using program correctly
   print("Invalid usage")
   sys.exit(0)   