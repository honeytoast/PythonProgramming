Name: Grace Hadiyanto
E-mail: ifoundparis@gmail.com
CPSC 223P
Assignment 1

Product: A program that finds the first 100,000 prime numbers.

Description: The program uses two methods to find the first 100,000 prime
             numbers. One method is by trial division and the other is by
             using the Sieve of Eratosthenes algorithm. It first does the
             Sieve of Eratosthenes 5 times and takes the average time it took
             to find 100,000 prime numbers. Then the method is repeated using
             trial division, and the time also recorded and printed.
	     
	     The sieve function starts off with a list of True values of the size
	     n. It takes the first number as the first factor and uses the variable index 	     that keeps track of every multiple of that factor in the list. The multiples 	     are crossed off/marked as False(composite), and continues doing so for
	     the next number until the end of the list. The returned list, if printed with 	     the output function, will show all the prime numbers up to n.

       	     Sample output:
             Finding 100000 prime numbers by Sieve of Eratosthenes where n = 5.
       	     Sieve of Eratosthenes took 1.866 seconds on average.

       	     Finding 100000 prime numbers by trial division where n = 5
             Trial division took 13.332 seconds on average.

Caution: I was only able to implement the Sieve of Eratosthenes algorithm
         to find prime numbers up until a certain range. 1299709 is the 100,000th 		 thousand prime number, so I initialized the list with size 1299708. It still 
         runs way faster than trial division though.

How to run: Open your terminal and make sure you are in the directory folder
            that contains "primes.py".
            Type "python3.3 primes.py" and press enter to start the program.
