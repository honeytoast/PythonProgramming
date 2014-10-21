#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment4

import random
import sys

class TreeNode:
    """A class of a node to be used in a binary tree. """

    __slots__ = { '_parent', '_left', '_right', '_data' }

    def __init__(self, parent, data):
        self._parent = parent
        self._left = None
        self._right = None
        self._data = data

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
        form_null = '\t{} [shape=point];\n\t{} -> {};\n'
        s = ''
        if self.left != None:
            s += form.format(self.data, self.left.data)
        else:
            s += form_null.format('null', self.data, 'null')
        if self.right != None:
            s += form.format(self.data, self.right.data)
        else:
            s += form_null.format('null', self.data, 'null')
        if self.parent != None:
            s += form.format(self.data, self.parent.data)
        return s


class Tree():
    """A binary tree class."""

    __slots__ = { '_root' }
    
    def __init__(self):
        self._root = None

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

    def isEmpty(self):
        return self.root == None

    def insert(self, key):
        location = self.root
        parent = None
        while location != None:
            parent = location
            if location.data > key:
                location = location.left
            else:
                location = location.right
        new_node = TreeNode(parent, key)
        if parent == None:
            self.root = new_node
        elif parent.data > key:
            parent.left = new_node
        else:
            parent.right = new_node
    
    def _find(self, node, key):
        while node != None and node.data != key:
            if key > node.data:
                node = node.right
            else:
                node = node.left
        return node

    def _localMin(self, start):
        node = start
        while node.left != None:
            node = node.left
        return node

    def _localMax(self, start):
        node = start
        while node.right != None:
            node = node.right
        return node

    def minimum(self):
        return self._localMin(self.root)
    
    def maximum(self):
        return self._localMax(self.root)

    # Returns the node containing the key(data), if no node has the same key, it
    # will return None
    def hasKey(self, key):
        return self._find(self.root, key)

    def remove(self, key):
        node = self.hasKey(key)
        if node != None:
            self._deleteNode(node)
            return True
        else:
            return False

    # Replaces subtree at node x with subtree at node y
    def _transplant(self, x, y):
        if x.parent == None:
            self.root = y
        elif x.isLeftChild():
            x.parent.left = y
        else:
            x.parent.right = y
        if y != None:
            y.parent = x.parent

    def _deleteNode(self, node):
        if node.left == None:
            self._transplant(node, node.right)
        elif node.right == None:
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
        del node

    # Traverses the tree in a preorder traversal, appending a string format of
    # the data of each node.
    def preorderTraversal(self, start, lst):
        if start != None:
            lst.append(str(start))
            if start.left != None:
                self.preorderTraversal(start.left, lst)
            if start.right != None:
                self.preorderTraversal(start.right, lst)

# This function takes a list of data from traversal of a tree and uses string
# manipulation to format it into the correct syntax for the DOT language.
# nc - total null count
# lnc - local null count
# ncs - total null count as a string
# ds - formatted string of the data up to the end of the second null
# n1, n2, n3, n4 - the index at the end of each null
def listToString(lst):
    s = ''
    nc = 0
    for i in lst:
        data = str(i)
        lnc = data.count('null')
        if lnc != 0:
            n1 = data.find('null') + 4
            n2 = data.find('null', n1 + 1) + 4
            end = len(data)
            nc += 1
            ds = data[0:n1] + str(nc) + data[n1:n2] + str(nc)
            if lnc == 2:
                data = ds + data[n2:end]
            elif lnc == 4:
                nc += 1
                ncs = str(nc)
                n3 = data.find('null', n2 + 1) + 4
                n4 = data.find('null', n3 + 1) + 4
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
    t = Tree( )
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
