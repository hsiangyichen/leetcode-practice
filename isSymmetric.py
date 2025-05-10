# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# def isSymmetric(self, root):
#     def symmetric(l, r):
#         if not l and not r:
#             return True
#         if not l or not r:
#             return False
#         if l.val != r.val:
#             return False
#         return symmetric(l.left, r.right) and symmetric(l.right, r.left)
#     return symmetric(root.left, root.right)