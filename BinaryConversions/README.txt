Name: Grace Hadiyanto
E-mail: ifoundparis@gmail.com
CPSC 223P
Assignment 2

Product: 2 Programs for converting binary to characters, and characters to binary


Description: "char2bin.py" takes in a string as its argument and will print out
             the binary representation of the characters in the string, including
             but not limited to spaces and punctuation.
             
             "bin2char.py" does the opposite and will take in binary values and
             print out the ASCII representation of the string.


How to run: Open your terminal and make sure you are in the directory that
            contains "char2bin.py" and "bin2char.py"

   To convert a string into binary: type char2bin.py "{message here}"
   
   To go from binary into an ASCII representation: type bin2char.py {binary here}

   Sample conversion from characters to binary:
   
        # command
        python3.3 char2bin.py "Sometimes, you have to roll the hard six."

        # output
        
        01010011 01101111 01101101 01100101 01110100 01101001 
        01101101 01100101 01110011 00101100 00100000 01111001 
        01101111 01110101 00100000 01101000 01100001 01110110 
        01100101 00100000 01110100 01101111 00100000 01110010 
        01101111 01101100 01101100 00100000 01110100 01101000 
        01100101 00100000 01101000 01100001 01110010 01100100 
        00100000 01110011 01101001 01111000 00101110
   
   Sample conversion from binary to ASCII representation:

        # command
        python3.3 bin2char.py 01010011 01101111 01101101 01100101 01110100 
        01101001 01101101 01100101 01110011 00101100 00100000 01111001 01101111 
        01110101 00100000 01101000 01100001 01110110 01100101 00100000 01110100 
        01101111 00100000 01110010 01101111 01101100 01101100 00100000 01110100 
        01101000 01100101 00100000 01101000 01100001 01110010 01100100 00100000 
        01110011 01101001 01111000 00101110

        # output
        Sometimes, you have to roll the hard six.


Caution: For converting a string into binary, make sure that your message is
         in one string. That means that the whole message must be encapsulated
         by a pair of quotations.

         For converting binary into an ASCII representation, make sure that
         each binary representation of the character is separated by only spaces.
         
