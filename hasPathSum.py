# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that 
# adding up all the values along the path equals targetSum.

# def hasPathSum(self, root, targetSum):
#     def sumUp(node, currSum):
#         if not node:
#             return False
        
#         currSum += node.val

#         if not node.left and not node.right:
#             if currSum == targetSum:
#                 return True
#             elif currSum > targetSum:
#                 return False
#         return sumUp(node.left, currSum) or sumUp(node.right, currSum)

#     return sumUp(root, 0)