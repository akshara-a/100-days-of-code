# Hackerrank

# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        print(root.info, end = " ")
        inOrder(root.right)
