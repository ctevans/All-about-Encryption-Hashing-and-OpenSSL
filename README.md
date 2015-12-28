# All-about-Encryption-Hashing and OpenSSL
Given Encrypted Files, break them. Given passwords hashed with various hash functions, find the original passwords. Use encryption and hashing on our own data. Also using the tool OpenSSL.

## This has multiple parts to itself, and so I will explain here what each is and it's purpose.

##Part 1 and Part 2:
Given an encrypted file (ciphertext1) encrypted with a variation of the Vignere Cipher, the goal was to break the encryption and reveal the original contents of the file before encryption.
 
The encryption scheme is depited in this image.
http://imgur.com/KQWgUKQ

Using the program created, part1_2.py, the encrypted files were processed and decrypted. 

This ended up yielding two results:
plaintext1: A short text file containing Yesterday by W. S. Merwin.
plaintext2: A rich text file containing "Boycott Action Kit", an 18 page document containing numerous colored images, hyperlinks and in-depth formatting.

Furthermore the keys used to encrypt the documents were also obtained:

ciphertext1 password: 4fathers

ciphertext2 password: Pass_TheBoycottActionKit_GentBelgium

##Part 3:
Here we have a host of files that are likely meaningless to most, hopefully I can dispell that here.

Located within, there is a created plaintext file with 10 repetitions of characters (no whitespace) of 01234567.

Then using the tool OpenSSL we then encrypted the created plaintext file with: ECB, CBC, CFB, OFB with DES. This created the numerous ciphertext files seen in the folder. We then explained the differences produced by the various encryption methods in the writeup file.

Next the impacts of changing the file with an "error" were desired, changing the plaintext file fed into OpenSSL producing the various "error" files located within.

Lastly in this section the goal was to take ciphertext3 which was encrypted with DES in ECB mode and then obtain how many students were in the original file, produce a modified version of the file where the first and second student records were swapped, obtain the identity of which student was the one that recieved the scholarship.
