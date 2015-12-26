g = [open('2EncryptFile'+str(i+1), 'w') for i in range(8)]

for i in range(8*7):
    p = 24*" "    
    
    n = 8* " "
    
    g[i%8].write('%s%s'%(n,p))
    
for i in range(8):
    g[i].write(str(i))
    
for i in g:
    i.close()