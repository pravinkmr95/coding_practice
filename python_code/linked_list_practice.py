import pdb


class LinkedList:
    def __init__(self, num):
        self.data = num
        self.next = None


def linked_list_insertion_front(head, num):
    node = LinkedList(num)
    node.next = head
    return node


def linked_list_insertion_end(curr, number):
    if not curr:
        return LinkedList(number)
    temp = curr
    while curr.next:
        curr = curr.next
    curr.next = LinkedList(number)
    return temp


def linked_list_insertion_after_node(number, node):
    if not node:
        return
    curr = LinkedList(number)
    temp = node.next
    node.next = curr
    curr.next = temp


def print_linked_list(curr):
    if curr is None:
        return
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print("")


def delete_number(head, number):
    curr = head
    if not head or (head.data == number and not head.next):
        return None
    if head.data == number:
        head = head.next

    prev = None
    while curr and curr.data != number:
        prev = curr
        curr = curr.next
    if prev and curr:
        prev.next = curr.next
    return head


def reverse_linkedlist(curr):
    prev = None
    while curr:
        next_ele = curr.next
        curr.next = prev
        prev = curr
        curr = next_ele
    return prev


def reverse_linkedlist_rec(curr):
    # pdb.set_trace()
    if curr is None or curr.next is None:
        return curr
    res = reverse_linkedlist_rec(curr.next)
    # print("res.data", res.data)
    # print("curr.data", curr.data)
    curr.next.next = curr
    # print("curr.next.data", curr.next.data)
    curr.next = None
    return res


def rotate_ll(curr, k):
    if k <= 0:
        return
    curr_head = curr
    temp = None
    while curr.next:
        k -= 1
        if k == 0:
            temp = curr
        curr = curr.next
    if temp:
        new_head = temp.next
        temp.next = None
        # print(curr_head.data)
        curr.next = curr_head
        return new_head
    else:
        return curr_head


def remove_duplicates_sorted_ll(curr):
    while curr and curr.next:
        next_node = curr.next
        if next_node.data == curr.data:
            temp = next_node.next
            curr.next = temp
        else:
            curr = curr.next


def pairwise_swap(curr):
    next_head = curr.next
    prev = None
    while curr and curr.next:
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = curr
        if prev:
            prev.next = next_node
        prev = curr
        curr = curr.next
        # print("curr.data", curr.data)
        # print_linked_list(next_head)
    if next_head:
        return next_head
    else:
        return curr


def reverse_ll_in_group_of_k(curr, k):
    prev = None
    n = 0
    temp = curr
    while curr and n < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        n += 1
    if curr:
        temp.next = reverse_ll_in_group_of_k(curr, k)
    return prev


if __name__ == "__main__":
    head = None
    for i in range(1, 7):
        # num = int(input())
        head = linked_list_insertion_front(head, i*10)

    # print_linked_list(head)
    # head = linked_list_insertion_end(head, 10)
    # head = linked_list_insertion_end(head, 20)
    # head = linked_list_insertion_end(head, 30)
    # print_linked_list(head)
    # linked_list_insertion_after_node(50, head.next.next.next)
    # print_linked_list(head)
    # head = delete_number(head, 0)
    print_linked_list(head)
    head = reverse_linkedlist_rec(head)
    print_linked_list(head)
    head = rotate_ll(head, 7)
    print_linked_list(head)

    n3 = LinkedList(60)
    head.next.next.next.next.next.next = n3
    # print_linked_list(head)
    # print(head.next.next.next.next.data)
    n2 = LinkedList(30)
    temp2 = head.next.next.next
    # print("temp2", temp2.data)
    head.next.next.next = n2
    n2.next = temp2

    n1 = LinkedList(10)
    n1.next = head
    head = n1
    print("before removing duplicated")
    print_linked_list(head)
    remove_duplicates_sorted_ll(head)
    print("after removing duplicated")
    print_linked_list(head)
    # head1 = LinkedList(10)
    # head1.next = LinkedList(10)
    # # head1.next.next = LinkedList(20)
    # print_linked_list(head1)
    # remove_duplicates_sorted_ll(head1)
    # print_linked_list(head1)
    head.next.next.next.next.next = None
    head = pairwise_swap(head)
    # head.next.next.next.next = None
    print("Before K reversal")
    print_linked_list(head)
    head = reverse_ll_in_group_of_k(head, k=4)
    print("After K reversal")
    print_linked_list(head)
