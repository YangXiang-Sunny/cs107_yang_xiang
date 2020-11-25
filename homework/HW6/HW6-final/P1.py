# HW6, Problem 1: BST Extensions
from enum import Enum


class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0

    def _removemin(self, node):
        if node.left is None:
            return node.right
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def min(self, node):
        if node.left is None:
            return node
        else:
            return self.min(node.left)

    def _remove(self, node, key):
        if node is None:
            raise KeyError("No such key is found!")
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.right is None:
                return node.left
            else:
                # Duplicate the node
                t = BSTNode(node.key, node.val)
                t.left = node.left
                t.right = node.right
                t.size = node.size

                # Modify the node
                node = self.min(t.right)
                node.right = self._removemin(t.right)
                node.left = t.left

        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.index = 0
        self.traversal = []

        # Calculate traversal
        if traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        elif traversalType == DFSTraversalTypes.INORDER:
            self.inorder(tree)
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(tree)
        else:
            raise KeyError("Traversal Type ERROR!")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            node = self.traversal[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1

        return node

    def inorder(self, bst: BSTTable):

        def inorder_traverse(node):
            if node is None:
                return
            else:
                inorder_traverse(node.left)
                if node not in self.traversal:
                    self.traversal.append(node)
                inorder_traverse(node.right)

        inorder_traverse(bst._root)
        return

    def preorder(self, bst: BSTTable):

        def preorder_traverse(node):
            if node is None:
                return
            else:
                if node not in self.traversal:
                    self.traversal.append(node)
                preorder_traverse(node.left)
                preorder_traverse(node.right)

        preorder_traverse(bst._root)
        return

    def postorder(self, bst: BSTTable):

        def postorder_traverse(node):
            if node is None:
                return
            else:
                postorder_traverse(node.left)
                postorder_traverse(node.right)
                if node not in self.traversal:
                    self.traversal.append(node)

        postorder_traverse(bst._root)
        return


# if __name__ == "__main__":
#     # t = BSTTable()
#     # t.put(5, 'a')
#     # t.put(1, 'b')
#     # t.put(2, 'c')
#     # t.put(0, 'd')
#     # print(t._root)
#
#     # # Test BST.removemin()
#     # print(t._removemin(t._root))
#
#     # # Test BST.remove()
#     # t.remove(5)
#     # print(t)
#     # t.remove(1)
#     # print(t)
#     # t.remove(10)
#
#     # Test DFSTraversal
#     input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
#     bst = BSTTable()
#     for key, val in input_array:
#         bst.put(key, val)
#     traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
#     for node in traversal:
#         print(str(node.key) + ', ' + node.val)


