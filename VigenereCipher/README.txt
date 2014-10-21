Name: Grace Hadiyanto
E-mail: ifoundparis@gmail.com
CPSC 223P
Assignment 2

Product: 1 module - “cipher.py”
	       2 programs - “vigenerecipher.py” and vigeneredecipher.py” for ciphering
                      and deciphering a Vigenere Cipher.
	       3 sample text files - “sample.txt”: original message #keyword: lime
                               “sample-cipher.txt”: ciphered message
                               “sample-cipher-clear.txt”: deciphered message


Description: I made a module "cipher.py" that includes all the functions needed
             for ciphering, deciphering, and formatting the message. The module
             is crucial for the two programs. 
             
             A message from a text file will be read, and ciphered/deciphered
             using a keyword which provides an index into the corresponding
             shifted alphabet. The program does the shift letter by letter.
             If there are more letters in the message than there are in the
             keyword, the keyword will be repeated until each of the letters
             in the message has an assigned shift by the keyword.

             For example:   keyword - lime
                            message - The eagle has landed
                                      lim elime lim elimel

             The programs I have created will accept a message in a text file,
             and after ciphering/deciphering, it will keep track of the 
             case-matching of the characters and common special 
             characters/formatting such as tabs, commas, and periods. The
             resulting ciphered/deciphered message will be output to a file.


How to run: Open your terminal and make sure you are in the directory folder that
            contains "cipher.py", "vigenerecipher.py", and "vigeneredecipher.py".

   To cipher a message: type "python3.3 vigenerecipher.py {your text file here}"
                        The program will then ask you for a keyword.
                        Enter the keyword you want to use and make sure to
                        remember it for deciphering the message.

   To decipher a message: "python3.3 vigeneredecipher.py {your text file here}"
                           The program will then ask you for a keyword.
                           You must enter the keyword that matches the keyword
                           used to cipher the original message.

   Example of cipher:

             # sample.txt
             This is a sample message that will be ciphered.
             “Do you wanna build a snowman?”
             It doesn't look very interesting now but,
             It will look very cryptic afterwards.
             I am demonstrating, that “I” can use special characters.
             And they will be redisplayed in the output, like quotations,
	               or even tabs.
             Python is cool.

             # command
             python3.3 vigenerecipher.py sample.txt

             # output
             Enter a keyword: lime
             Cipher successful. Please check sample-cipher.txt

             # sample-cipher.txt
             Epuw ta m wlubpp uqwdisi epmx hqxp mm omapqvpl.
             “Ps jwg alvze mcupo i erzeyey?”
             Qf hzmer'e tasv dqvj qzxpzqweqzk ywi ffb,
             Ux hqxp wwao gmdc nzkteqo eqbqvhidhd.
             Q mq omysyafvlburr, btee “Q” oey cei dxqgtix gsidenbqvd.
             Izh epqc hqxp mm dioqetwikio qz xsm ayexgx, wqwi bcaxlbusya,
	               av pdqr einw.
             Agflzv uw nwap.

Caution: The decipher program will not output the message you expect it to if you
         type in a keyword that did not match the same keyword used to
         cipher the original message.

         Do not put any spaces in the keyword. The keyword can only be one word,
         hence keyword, not keywords.

         Have your message in one text file only.
         The program only works to decipher or cipher one text file at a time.

         Do not put multiple text files to be ciphered/deciphered.

         Any unrecognized special characters in the message will be ciphered/
         deciphered as a space. To avoid this, the user may add the special
         character they want to see in this format 'special character', in
         the special_characters set in "cipher.py". After saving the file,
         upon running the ciphering/deciphering program again, they shall see
         the special character that was not included before.
