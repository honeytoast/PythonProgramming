Name: Grace Hadiyanto
E-mail: ifoundparis@gmail.com
CS223P
Assignment 3

Product: A class for processing 2D-coordinate information.

Description: The class called Cartesian2D accepts and stores a pair of 2D
             coordinates. 
             
             The following methods are supported by the Cartesian2D class:
             - Multiplication with a scalar
             - Addition with another Cartesian2D instance
             - Subtraction with another Cartesian2D instance
             - Comparison with another Cartesian2D instance
             - Computation of the distance between itself and another Cartesian2D
             - Normalizing of the Cartesian2D instance itself
             - Measuring the length of the Cartesian2D instance itself

             A function outside of the class called dot takes the dot product
             of 2 Cartesian2D instances.

             The assignment main() is also included.      

How to run: Open your terminal and make sure you are in the directory containing
            cartesian_demo.py
            Your command should be: python3.3 cartesian_demo.py

Caution: When printing a Cartesian2D object: There is no way for me to overload
         the string representation inside the class with the specific name of
         the instance of the object. To avoid confusion, you can put the name of
         the instance in a string in the main function before printing.

         For example, if you want to print the Cartesian2D named d :
         instead of typing this in the main:   print(d)
         one would type:                       'd is {}'.format(d)
