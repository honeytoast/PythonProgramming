#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 2

#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 2

import sys
import cipher

def main():
    keyword = input('Enter a keyword: ')
    
    # Stores the name of the input file and reads its contents
    infile_name = str(sys.argv[1])
    infile = open(sys.argv[1], 'r')
    secret_intel = infile.read()
    infile.close()
    
    # Takes the keyword, contents of the file, and creates a ciphered message
    key_values = cipher.alphaIndex(keyword)
    intel_values = cipher.alphaIndex(secret_intel)
    code = cipher.encodeList(intel_values, key_values)
    coded_message = cipher.transcribe(secret_intel, code)
    
    # Writes the ciphered message out into a file
    outfile_name = cipher.outFileName(infile_name, 'cipher')
    outfile = open(outfile_name, 'w')
    output = cipher.listToString(coded_message)
    outfile.write(cipher.formatString(secret_intel, output))
    outfile.close()
    
    print('Cipher successful. Please check {}'.format(outfile_name))
    
if __name__ == '__main__':
    main()
