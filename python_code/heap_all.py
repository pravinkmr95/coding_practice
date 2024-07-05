import heapq


class Heap:
    def __init__(self):
        self.heap_list = []
        self.heap_size = 0

    def left_child(self, i):
        return 2*i + 1

    def right_child(self, i):
        return 2*i + 2

    def parent(self, i):
        return (i-1)//2

    def heap_push(self, number):
        self.heap_list.append(number)
        self.heap_size += 1
        self.upward(self.heap_size - 1)

    def heap_pop(self):
        if self.heap_size > 0:
            print(self.heap_list[0])
            self.heap_list[0], self.heap_list[-1] = self.heap_list[-1], self.heap_list[0]
            self.heap_size -= 1
            self.heap_list.pop()
            self.downward(0)

    def downward(self, i):
        if i < self.heap_size:
            max_element_index = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < self.heap_size and self.heap_list[max_element_index] < self.heap_list[left]:
                max_element_index = left
            if right < self.heap_size and self.heap_list[max_element_index] < self.heap_list[right]:
                max_element_index = right
            if max_element_index != i:
                self.heap_list[max_element_index], self.heap_list[i] = (self.heap_list[i],
                                                                        self.heap_list[max_element_index])
                self.downward(max_element_index)

    def upward(self, i):
        if i > 0:
            parent = self.parent(i)
            if self.heap_list[i] > self.heap_list[parent]:
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
                self.upward(parent)

    def heapify(self, arr, i, n):
        if i < n:
            max_element_index = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < n and arr[max_element_index] < arr[left]:
                max_element_index = left
            if right < n and arr[max_element_index] < arr[right]:
                max_element_index = right
            if max_element_index != i:
                arr[max_element_index], arr[i] = (arr[i], arr[max_element_index])
                self.heapify(arr, max_element_index, n)

    def min_heapify(self, i):
        if i < self.heap_size:
            min_element_index = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < self.heap_size and self.heap_list[min_element_index] > self.heap_list[left]:
                min_element_index = left
            if right < self.heap_size and self.heap_list[min_element_index] > self.heap_list[right]:
                min_element_index = right
            if min_element_index != i:
                self.heap_list[min_element_index], self.heap_list[i] = (self.heap_list[i],
                                                                        self.heap_list[min_element_index])
                self.downward(min_element_index)

    def print_heap(self):
        print(self.heap_list)


def heap_sort(arr):
    n = len(arr)
    heapq = Heap()
    for i in range(n//2-1, -1, -1):
        heapq.heapify(arr, i, n)
    # print("arr", arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapq.heapify(arr, 0, i)


def heap_sort_heapq(arr):
    result = []
    heapq.heapify(arr)
    while arr:
        result.append(heapq.heappop(arr))
    for num in result:
        arr.append(num)


def kth_smallest(arr, k):
    result = -1
    heapq.heapify(arr)
    for i in range(k):
        result = arr[0]
        heapq.heappop(arr)
    return result


if __name__ == "__main__":
    heap = Heap()
    numbers_list1 = [1, 0, 4, 6, 8, 10, 0]
    for num in numbers_list1:
        heap.heap_push(num)
    heap.print_heap()
    # for i in range(len(numbers_list)):
    #     heap.heap_pop()
    #     heap.print_heap()
    # numbers_list2 = [1, 0, 4, 6, 8, 10, 0]
    # heap_sort(numbers_list2)
    # print(numbers_list2)
    numbers_list3 = [1, 0, 4, 6, 8, 10, 0, -1, 10, 22, 50]
    heap_sort_heapq(numbers_list3)
    print(numbers_list3)
    input_list = [7, 10, 4, 3, 20, 15]
    k = 3
    print(kth_smallest(input_list, k))
