THANK YOU FOR USING Part1&2.txt

To use the program, simply do the following

On the command line:

STEP1:

Python Part1&2.py  ciphertext* ->Displays the possible keys with all possible values at each position.
Python Part1&2.py  ciphertext* -p “HEADER” -> searches the same thing as the previous line, but with a little bit of known plaintext format so to make the password search faster

STEP2:
Python Part1&2.py  ciphertext* -d “key**” -> decryption of Cipher text based on the inputted KEY

*= the ciphertext we are decrypting.  Type ciphertext1 for part1 and ciphertext2 for part2.
**= type in one of the possible keys obtained in STEP1.
