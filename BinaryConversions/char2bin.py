#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 2

import sys

def main():

    s = sys.argv[1]
    l = []

    for c in s:
        bin_str = bin(ord(c))
        zero_count = 8 - len(bin_str[2:])
        bin_str = zero_count * '0' + bin_str[2:]
        l.append(bin_str)

    # Formats the list to output the binary representations of a character
    # by 6 representations at a time
    for i, byte in enumerate(l):
        if i % 7 == 0:
            l.insert(i, '\n')
    print(' '.join(l))
        
if __name__ == '__main__':
    main()
