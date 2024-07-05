class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # The first element in preorder list is the root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root in inorder list
    mid = inorder.index(root_val)

    # Elements to the left of 'mid' are in the left subtree
    # Elements to the right of 'mid' are in the right subtree
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root


preorder = [3, 9, 20, 15, 7] # root, left, right
inorder = [9, 3, 15, 20, 7] # left root right

root = build_tree(preorder, inorder)

# Function to print tree in inorder to verify
def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)

print_inorder(root)
# Output should be: 9 3 15 20 7
