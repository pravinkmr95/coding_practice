import random
import sys


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def push_bst(root, data):
    if root is None:
        return TreeNode(data)
    if root.data <= data:
        root.right = push_bst(root.right, data)
    else:
        root.left = push_bst(root.left, data)
    return root


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    inorder(node.left)
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    inorder(node.left)
    inorder(node.right)
    print(node.data, end=" ")


def height_of_tree(node):
    if node is None:
        return 0
    left_h = height_of_tree(node.left)
    right_h = height_of_tree(node.right)
    return 1 + max(left_h, right_h)


def find_min(node):
    while node and node.left:
        node = node.left
    return node


def delete_node_bst(node, num):
    if node is None:
        return node
    if num < node.data:
        node.left = delete_node_bst(node.left, num)
    elif num > node.data:
        node.right = delete_node_bst(node.right, num)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = find_min(node.right)
        node.data = temp.data
        # del temp
        node.right = delete_node_bst(node.right, temp.data)
    return node


def is_identical(node1, node2):
    if node1 is None and node2 is None:
        return True
    if (node1 and node2 and node1.data == node2.data and is_identical(node1.left, node2.left)
            and is_identical(node1.right, node2.right)):
        return True
    return False


def mirror_tree(head):
    if head is None:
        return
    mirror_tree(head.left)
    mirror_tree(head.right)
    temp = head.left
    head.left = head.right
    head.right = temp


def isBST(root_node, left, right):
    # print(left, right)
    if root_node is None:
        return True
    if root_node.data < left or root_node.data > right:
        print("Coming here")
        print(left, right, root_node.data)
        return False
    return isBST(root_node.left, left, root_node.data - 1) and isBST(root_node.right, root_node.data+1, right)


if __name__ == "__main__":
    root = None
    delete_list = []
    for _ in range(6):
        number = random.randint(0, 100)
        root = push_bst(root, number)
        delete_list.append(number)
    inorder(root)
    print("")
    # preorder(root)
    # print("")
    # postorder(root)
    # print("")
    # print(height_of_tree(root))
    # for number in delete_list:
    #     print("Node deletion", number)
    #     root = delete_node_bst(root, number)
    #     inorder(root)
    #     print("")
    root1 = None
    for number in delete_list:
        root1 = push_bst(root1, number)
    inorder(root1)
    print("")
    print(is_identical(root, root1))
    # mirror_tree(root1)
    rr = TreeNode(48)
    rr.left = TreeNode(20)
    rr.right = TreeNode(90)
    rr.right.left = TreeNode(47)
    rr.right.left = TreeNode(95)
    inorder(rr)
    print("")
    print(isBST(rr, -sys.maxsize, sys.maxsize))
    # print(isBST(root, -sys.maxsize, sys.maxsize))
