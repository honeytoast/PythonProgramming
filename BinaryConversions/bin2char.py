#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 2

import sys

def main():
    bin_input = sys.argv
    i = 1
    l = []
    while i <= len(bin_input) - 1:
        # Converts the base-2 binary to its int value then to its ASCII char
        a = chr(int(bin_input[i], 2))  
        l.append(a)
        i += 1
    for a, v in enumerate(l):
        print(v, end='')
    print()

if __name__ == '__main__':
    main()
