class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#     a
#    / \
#   b   c
#  / \   \
# d   e   f

