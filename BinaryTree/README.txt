#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment4

Product: A binary tree class that outputs data in dot syntax to produce
         a graphical representation of itself using Graphviz. Sample outputs
	 in jpg are included.

Description: The user enters a number as part of the command line argument to
             run the program. The number will become the amount of nodes that
             gets put into the tree. A list containing a range of numbers from
             1 to the user number input will be randomly shuffled and inserted
             into the tree. 1/3 of the nodes will be removed and another 1/3
             will be removed afterwards, resulting in 3 different versions of
             the tree.
             
             Running the program will result in 3 files: a.dot b.dot c.dot
             a.dot - contains the first version of the binary tree
             b.dot - contains the second version of the tree after 1/3 of its
                     nodes are removed.
             c.dot - contains the third version of the tree after another 1/3 of 
                     its nodes are removed.
             
             The user can then use the .dot files as an input to the dot
             program to create a graphical representation of the tree in .pdf

             The tree will have nodes that are oval shaped. A point
             represents a none node.
             
How to run: > python3.3 binaryTree.py {}
            where {} is the number of nodes you wish to enter.

            After running the program, in the same directory, to see the tree,
            > dot -Tpdf -o {}.pdf {}.dot
            where the first {} is the name you want your pdf file to be and
            the second {} is the name of the .dot file input.

Caution: When using Graphviz, it will take longer to create a .pdf of the tree
         if it has a high number of nodes.
