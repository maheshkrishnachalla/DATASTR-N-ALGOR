# Binary Tree
from display_tree import print_tree
class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


node1  = Node(10)
node2  = Node(11)
node3  = Node(12)
node4  = Node(13)
node5  = Node(14)
node6  = Node(15)
node7  = Node(16)
node8  = Node(17)
node9  = Node(18)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left =  node6
node3.right = node7
node4.left = node8
node4.right = node9

#print(node1.data, node1.left.data, node1.right.data)
print_tree(node1, val='val', left='left', right='right')
