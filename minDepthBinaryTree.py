# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# def minDepth(self, root):

# Method 1: 
#     if not root:
#         return 0
#     if root.left and root.right:
#         return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
#     elif root.left and not root.right:
#         return 1 + self.minDepth(root.left)
#     elif root.right and not root.left:
#         return 1 + self.minDepth(root.right)
#     else:
#         return 1

# Method 2:
#     if not root:
#         return 0
#     if root.left and root.right:
#         return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
#     elif not root.left or not root.right:
#         return 1 + max(self.minDepth(root.left), self.minDepth(root.right))