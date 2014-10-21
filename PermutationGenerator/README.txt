#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment6

Product: A Permutation class that generates on demand all the permutations of a
         given list.

Description: The Permutation class is a generator that yields each permutation
             of a given list. The list is updated in place every time a new 
             permutation is found and the next permutation is based on the
             current permutation.
             The algorithm implemented by the class goes like this:
             First, it starts with a given list, say a, and sorts it.
             Yield that list as the first permutation.
            1. Yield the current list.  #for all other iterations after the first
            # A temporary list is made for storing indices to determine the
            max index that satisfy the conditions.
            2. Find the largest index i such that a[i] < a[i + 1],
                   if no index exists, the last yielded permutation was the last one,
                   and iteration stops.
            3. Find the largest index l such that a[i] < a[l].
            4. Swap the value of a[i] with a[l]
            5. Reverse the list from a[i + 1:]
               Continue 1-5 until all permutations are found.

            A main function is included that demonstrates its use on the list
            ['a','b','c'] to print all permutations of the list and to print
            only the first n permutations.
           
How to run: python3.3 Permutation.py


