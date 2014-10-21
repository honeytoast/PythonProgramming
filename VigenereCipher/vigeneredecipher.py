#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 2

import sys
import cipher

def main():
    keyword = input('What is the keyword?: ')

    # Stores the name of the input file and reads its contents
    infile_name = str(sys.argv[1])
    infile = open(sys.argv[1], 'r')
    cryptic_note = infile.read()
    infile.close()

    # Takes the keyword, contents of the file, and creates a deciphered message
    key_values = cipher.alphaIndex(keyword)
    cryptic_values = cipher.alphaIndex(cryptic_note)
    decoder = cipher.decodeList(cryptic_values, key_values)
    decoded_message = cipher.transcribe(cryptic_note, decoder)

    # Writes the deciphered message out into a file
    outfile_name = cipher.outFileName(infile_name, 'decipher')
    outfile = open(outfile_name, 'w')
    output = cipher.listToString(decoded_message)
    outfile.write(cipher.formatString(cryptic_note, output))
    outfile.close()

    print('Decipher successful. Please check {}'.format(outfile_name))

if __name__ == '__main__':
    main()
