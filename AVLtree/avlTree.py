#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment4

import sys
import random

class AvlNode:
    """A node class to be used for an AVL tree."""

    __slots__ = {'_parent', '_left', '_right', '_data', '_height'}

    def __init__(self, parent, data):
        self._parent = parent
        self._left = None
        self._right = None
        self._data = data
        self._height = 0

    # The 'parent' property
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, node):
        self._parent = node
    @parent.deleter
    def parent(self):
        del self._parent
    
    # The 'left' property
    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, node):
        self._left = node
    @left.deleter
    def left(self):
        del self._left
    
    # The 'right' property
    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, node):
        self._right = node
    @right.deleter
    def right(self):
        del self._right

    # The 'data' property
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value
    @data.deleter
    def data(self):
        del self._data
    
    # The 'height property
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height
    @height.deleter
    def height(self):
        del self._height
    
    
    def isLeftChild(self):
        return self.parent.left == self

    def isRightChild(self):
        return self.parent.right == self

    def isLeafNode(self):
        return self.left == None and self.right == None

    def hasOneChild(self):
        if self.left != None and self.right == None:
            return True
        elif self.left == None and self.right != None:
            return True
        else:
            return False

    def hasTwoChildren(self):
        return self.left != None and self.right != None

    def __str__(self):
        form = '\t{} -> {};\n'
        s = ''
        form_none = s + '\tNone [height=.25 width=.5 style=filled fontcolor=white fillcolor=black shape=box];\n'
        if self.left.data != None:
            s += form.format(self.data, self.left.data)
        else:
            s += form_none + form.format(self.data, 'None')
        if self.right.data != None:
            s += form.format(self.data, self.right.data)
        else:
            s += form_none + form.format(self.data, 'None')
        if self.parent.data != None:
            s += form.format(self.data, self.parent.data)
        return s


class AVLTree:
    """An AVL Tree class."""

    __slots__ = {'_root', '_none'}

    def __init__(self):
        self._none = AvlNode(None, None)
        self._none.left = self._none
        self._none.right = self._none
        self._none.parent = self._none
        self._root = self._none

    # The 'root' property
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, node):
        self._root = node

    # The 'none' property
    @property
    def none(self):
        return self._none
    @none.setter
    def none(self, node):
        self._none = node
    
    def hasKey(self, key):
        return self._find(self.root, key)

    def _localMin(self, node):
        if node == self.none:
            node = self.root
        while node.left != self.none:
            node = node.left
        return node
    
    def _localMax(self, node):
        if node == self.none:
            node = self.root
        while node.right != self.none:
            node = node.right
        return node

    def _find(self, node, key):
        while node != self.none and node.data != key:
            if key > node.data:
                node = node.right
            else:
                node = node.left
        return node

    def remove(self, key):
        node = self.hasKey(key)
        if node != self.none:
            self._deleteNode(node)
            return True
        else:
            return False

    # Replaces subtree at node x with subtree at node y
    def _transplant(self, x, y):
        if x.parent == self.none:
            self.root = y
        elif x.isLeftChild():
            x.parent.left = y
        else:
            x.parent.right = y
        if y != self.none:
            y.parent = x.parent

    def _deleteNode(self, node):
        if node.left == self.none:
            self._transplant(node, node.right)
        elif node.right == self.none:
            self._transplant(node, node.left)
        else:
            successor = self._localMin(node.right)
            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
        x = node.parent
        del node
        self.balance(x)

    def updateHeight(self, node):
        node.height = 1 + max(node.left.height, node.right.height)

    def balanceFactor(self, node):
        return node.left.height - node.right.height

    def leftRotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent == self.none:
            self.root = y
        else:
            if y.parent.left == x:
                y.parent.left = y
            elif y.parent.right == x:
                y.parent.right = y
        x.right = y.left
        if x.right != self.none:
            x.right.parent = x
        y.left = x
        x.parent = y
        self.updateHeight(x)
        self.updateHeight(y)

    def rightRotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent == self.none:
            self.root = y
        else:
            if y.parent.left == x:
                y.parent.left = y
            elif y.parent.right == x:
                y.parent.right = y
        x.left = y.right
        if x.left != self.none:
            x.left.parent = x
        y.right = x
        x.parent = y
        self.updateHeight(x)
        self.updateHeight(y)
    
    # To be used after each insert and deletion to keep the AVL balance property.
    # This function balances the node and all parent nodes tracing up to the root 
    # if their balance factor is not -1, 0, or 1.
    def balance(self, node):
        while node != self.none:
           self.updateHeight(node)
           if self.balanceFactor(node) >= 2:
               if self.balanceFactor(node.left) >= 0:
                   self.rightRotate(node)
               else:
                   # The balance factor of node.left is -1 meaning its right
                   # subtree is higher and requires a left rotation first on 
                   # node.left then a right rotation on node to regain balance.
                   self.leftRotate(node.left)
                   self.rightRotate(node)
           elif self.balanceFactor(node) <= -2:
               if self.balanceFactor(node.right) <= 0:
                   self.leftRotate(node)
               else:
                   # The balance factor of node.right is 1 meaning its left
                   # subtree is higher and requires a right rotation first on
                   # node.right then a left rotation on node to regain balance.
                   self.rightRotate(node.right)
                   self.leftRotate(node)
           node = node.parent

    def insert(self, data):
        x = self.root
        y = self.none
        node = AvlNode(self.none, data)
        while x != self.none:
            y = x
            if x.data > data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.none:
            self.root = node
        elif y.data > data:
            y.left = node
        else:
            y.right = node
        node.left = self.none
        node.right = self.none
        self.balance(node)

    def preorderTraversal(self, start, lst):
        if start != self.none:
            lst.append(str(start))
            if start.left != self.none:
                self.preorderTraversal(start.left, lst)
            if start.right != self.none:
                self.preorderTraversal(start.right, lst)

# This function takes a list of data from traversal of a tree and converts it
# into a readable and formatted string for the DOT language.
# nc - total none count
# lnc - local none count
# ncs - total none count as a string
# ds - formatted string of the data up to the end of the second none
# n1, n2, n3, n4 - the index at the end of each none
def listToString(lst):
    s = ''
    nc = 0
    for i in lst:
        data = str(i)
        lnc = data.count('None')
        if lnc != 0:
            n1 = data.find('None') + 4
            n2 = data.find('None', n1 + 1) + 4
            end = len(data)
            nc += 1
            ds = data[0:n1] + str(nc) + data[n1:n2] + str(nc)
            if lnc == 2:
                data = ds + data[n2:end]
            elif lnc == 4:
                nc += 1
                ncs = str(nc)
                n3 = data.find('None', n2 + 1) + 4
                n4 = data.find('None', n3 + 1) + 4
                data = ds + data[n2:n3] + ncs + data[n3:n4] + ncs + data[n4:end]
        s += data
    return s
        
def writeTree(tree, file_name):
    file_name.write('digraph BST{\n')
    file_name.write('\tnode [fontsize=11 fontname="Helvetica"];\n')
    file_name.write('\tedge [arrowhead=vee];\n')
    lst = []
    tree.preorderTraversal(tree.root, lst)
    file_name.write(listToString(lst))
    file_name.write('}')

def main():
    if len(sys.argv) < 2:
        print('Please provide the number of keys to enter.')
        sys.exit(1)
    s = int(sys.argv[1])
    parts = int(s/3)
    t = AVLTree( )
    r = list(range(1,s+1))

    print('Randomly inserting the numbers from 1 to {}.'.format(len(r)))

    random.shuffle(r)
    
    for i in r:
        print('inserted {}'.format(i))
        t.insert(i)
    f = open('a.dot', 'w')
    writeTree(t, f)
    f.flush( )
    f.close( )
    random.shuffle(r)

    for n in range(1, 3):
        m = r[(n-1) * parts : (n * parts)]
        print(len(m))
        for i in m:
            print('removed {}'.format(i))
            v = t.remove(i)
            if v:
                print('\tcompleted.')
            else:
                print('\terror.')
        c = chr(n + 97)
        filename = str(c) + '.dot'
        f = open(filename, 'w')
        writeTree(t, f)
        f.flush( )
        f.close( )
    
if __name__ == '__main__':
    main()
