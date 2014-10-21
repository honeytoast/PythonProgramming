#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment4

import random
import sys

RED = 'red'
BLACK = 'black'

class RedBlackNode:
    """A node class used for a Red-Black Tree."""

    __slots__ = {'_color', '_data', '_parent', '_left', '_right'}

    def __init__(self, color, data):
        self._color = color
        self._data = data
        self._parent = None
        self._left = None
        self._right = None

    # The 'color' property
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    @color.deleter
    def color(self):
        del self._color

    # The 'data' property
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data
    @data.deleter
    def data(self):
        del self._data

    # The 'parent' property
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, parent):
        self._parent = parent
    @parent.deleter
    def parent(self):
        del self._parent

    # The 'left' child property
    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, left):
        self._left = left
    @left.deleter
    def left(self):
        del self._left

    # The 'right' child property
    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, right):
        self._right = right
    @right.deleter
    def right(self):
        del self._right
    
    def isRed(self):
        return self.color == RED

    def isBlack(self):
        return self.color == BLACK

    def __repr__(self):
        return '{}({})'.format(self.__class__, self.data)

    def __str__(self):
        form = '\t{} -> {};\n'
        s = '\t{} [style="filled" fillcolor={}];\n'.format(self.data, self.color)
        form_null = s + '\tNone [height=.25 width=.5 style=filled fillcolor=black shape=box];\n'
        if self.left.data != None:
            s += form.format(self.data, self.left.data)
        else:
            s += form_null + form.format(self.data, 'None')
        if self.right.data != None:
            s += form.format(self.data, self.right.data)
        else:
            s += form_null + form.format(self.data, 'None')
        if self.parent.data != None:
            s += form.format(self.data, self.parent.data)
        return s

class RedBlackTree:
    """ A Red-Black Tree class."""

    __slots__ = {'_root', '_none'}

    def __init__(self):
        self._none = RedBlackNode(BLACK, None)
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
    @root.deleter
    def root(self):
        del self._root

    # The 'none' property
    @property
    def none(self):
        return self._none
    @none.setter
    def none(self, node):
        self._none = node
    @none.deleter
    def none(self):
        del self._none

    def isEmpty(self):
        return self.root == self.none

    def hasKey(self, key):
        return self._find(self.root, key)

    def minimum(self):
        return self._localMin(self.root)
    
    def maximum(self):
        return self._localMax(self.root)

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

    def _leftRotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.none:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == self.none:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y
    
    def _rightRotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.none:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == self.none:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insert(self, data):
        x = self.root
        y = self.none
        node = RedBlackNode(BLACK, data)
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
        node.color = RED
        self._insertFixup(node)

    def _insertFixup(self, node):
        while node.parent.isRed():
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.isRed():
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._leftRotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rightRotate(node.parent.parent)
            else: 
                y = node.parent.parent.left
                if y.isRed():
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rightRotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._leftRotate(node.parent.parent)
        self.root.color = BLACK

    def _transplant(self, x, y):
        if x.parent == self.none:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent

    def remove(self, key):
        node = self.hasKey(key)
        if node != self.none:
            self._deleteNode(node)
            return True
        else:
            return False

    def _deleteNode(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.none:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.none:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._localMin(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == BLACK:
            self._deleteFixup(x)
        del node

    def _deleteFixup(self, node):
        while node != self.root and node.isBlack():
            if node == node.parent.left:
                w = node.parent.right
                if w.isRed():
                    w.color = BLACK
                    node.parent.color = RED
                    self._leftRotate(node.parent)
                    w = node.parent.right
                if w.left.isBlack() and w.right.isBlack():
                    w.color = RED
                    node = node.parent
                else:
                    if w.right.isBlack():
                        w.left.color = BLACK
                        w.color = RED
                        self._rightRotate(w)
                        w = node.parent.right
                    w.color = node.parent.color
                    node.parent.color = BLACK
                    w.right.color = BLACK
                    self._leftRotate(node.parent)
                    node = self.root
            else:
                w = node.parent.left
                if w.isRed():
                    w.color = BLACK
                    node.parent.color = RED
                    self._rightRotate(node.parent)
                    w = node.parent.left
                if w.left.isBlack() and w.right.isBlack():
                    w.color = RED
                    node = node.parent
                else:
                    if w != self.none and w.left.isBlack():
                        w.right.color = BLACK
                        w.color = RED
                        self._leftRotate(w)
                        w = node.parent.left
                    w.color = node.parent.color
                    node.parent.color = BLACK
                    w.left.color = BLACK
                    self._rightRotate(node.parent)
                    node = self.root
        node.color = BLACK
    
    def preorderTraversal(self, start, lst):
        if start != self.none:
            lst.append(str(start))
            if start.left != self.none:
                self.preorderTraversal(start.left, lst)
            if start.right != self.none:
                self.preorderTraversal(start.right, lst)

# This function takes a list of data from traversal of a tree and uses string
# manipulation to format it into the correct syntax for the DOT language.
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
                nc +=1
                ncs = str(nc)
                n3 = data.find('None', n2 + 1) + 4
                n4 = data.find('None', n3 + 1) + 4
                data = ds + data[n2:n3] + ncs + data[n3:n4] + ncs + data[n4:end]
        s += data
    return s
        
def writeTree(tree, file_name):
    file_name.write('digraph BST{\n')
    file_name.write('\tnode [fontsize=11 fontcolor="white" fontname="Helvetica"];\n')
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
    t = RedBlackTree( )
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
