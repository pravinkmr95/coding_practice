import random
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def bst_node_insertion(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = bst_node_insertion(root.left, data)
    else:
        root.right = bst_node_insertion(root.right, data)
    return root


def left_view(root, level, store):
    if root is None:
        return
    if store[0] == level:
        store[0] += 1
        print(root.data, end=" ")
    # print(root.data, " ", level, " ", str(store))
    left_view(root.left, level + 1, store)
    left_view(root.right, level + 1, store)


def level_order_traversal(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        for i in range(len(queue)):
            top = queue.popleft()
            if i == 0: # right view
                print(top.data, end=" ")
            if top.right:
                queue.append(top.right)
            if top.left:
                queue.append(top.left)
        # print()


def zig_zag_traversal(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    flag = False
    while queue:
        for i in range(len(queue)):
            top = queue.popleft()
            print(top.data, end=" ")
            if flag:
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
                flag = True
            else:
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                flag = False
        print()


def vertical_order_traversal(root):
    if root is None:
        return
    final_out = []
    queue = deque()
    queue.append((root, 0, 0))
    output = defaultdict(list)
    min_ver = 0
    max_ver = 0
    while queue:
        for i in range(len(queue)):
            curr, level, ver = queue.popleft()
            min_ver = min(min_ver, ver)
            max_ver = max(max_ver, ver)
            output[ver].append(([level, curr.data]))
            if curr.left:
                queue.append((curr.left, level + 1, ver - 1))
            if curr.right:
                queue.append((curr.right, level + 1, ver + 1))
    # print(output)
    for i in range(min_ver, max_ver + 1):
        out = sorted(output[i], key=lambda x: (x[0], x[1]))
        final_out.append([x[1] for x in out])
    return final_out


def left_traversal(root, output):
    if root is None:
        return
    if root.left:
        output.append(root.data)
        left_traversal(root.left, output)
    elif root.right:
        output.append(root.data)
        left_traversal(root.right, output)


def leaf_traversal(root, output):
    if root is None:
        return
    leaf_traversal(root.left, output)
    if root.left is None and root.right is None:
        output.append(root.data)
    leaf_traversal(root.right, output)


def right_reverse_traversal(root, output):
    if root is None:
        return
    if root.right:
        right_reverse_traversal(root.right, output)
        output.append(root.data)
    elif root.left:
        right_reverse_traversal(root.left, output)
        output.append(root.data)


def boundary_traversal(root):
    if root is None:
        return
    output = []
    left_traversal(root, output)
    leaf_traversal(root, output)
    right_reverse_traversal(root.right, output)
    return output


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)


if __name__ == "__main__":
    root = None
    for data in [46, 64, 78, 63, 53, 30, 32, 11, 0, 31]:
        # data = random.randint(10, 100)
        # print(data)
        root = bst_node_insertion(root, data)
    store = [0]
    # left_view(root, 0, store)
    # print(store)
    # level_order_traversal(root)
    # zig_zag_traversal(root)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.left.right = TreeNode(8)
    root.left.left.right.left = TreeNode(9)
    root.left.left.right.left.left = TreeNode(10)
    root.left.left.right.left.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)

    # print(vertical_order_traversal(root))
    inorder_traversal(root)
    print()
    print(boundary_traversal(root))
