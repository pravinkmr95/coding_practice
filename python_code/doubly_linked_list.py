class DLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def push(curr, number):
    if curr is None:
        return DLNode(number)
    else:
        new_node = DLNode(number)
        new_node.next = curr
        curr.prev = new_node
        return new_node


def print_DLL(curr):
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print("")


def print_DLL_rev(curr):
    while curr:
        print(curr.data, end=" ")
        curr = curr.prev
    print("")


def reverse_DLL(curr):
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        curr.prev = next_node
        prev = curr
        curr = next_node
    return prev


if __name__ == "__main__":
    head = None
    for i in range(1, 7):
        head = push(head, i*10)
    # print_DLL(head)
    # print_DLL_rev(head.next.next.next.next)
    print("Before Reverse")
    print_DLL(head)
    head = reverse_DLL(head)
    print("after Reverse")
    print_DLL(head)
    # print_DLL_rev(head.next.next.next.next)
