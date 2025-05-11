# Given the root of a binary tree, return the inorder traversal of its nodes' values.
def inorderTraversal(self, root):
    # left, root, right
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result

# Given the root of a binary tree, return the preorder traversal of its nodes' values.
def preorderTraversal(self, root):
    # root, left, right
    result = []
    def preorder(node):
        if not node:
            return
        result.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return result


# Given the root of a binary tree, return the postorder traversal of its nodes' values.
def postorderTraversal(self, root):
    # left, right, root
    result = []
    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        result.append(node.val)
    postorder(root)
    return result