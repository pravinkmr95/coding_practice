import heapq
class Heap:
    def __init__(self):
        self.heap_list = []
        self.heap_size = 0

    def parent_node(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2*i + 1

    def right_child(self, i):
        return 2*i + 2

    def print_heap(self):
        print(self.heap_list)

    def top(self):
        return self.heap_list[0]

    def insert(self, number):
        self.heap_list.append(number)
        self.heap_size += 1
        current = self.heap_size - 1
        parent = self.parent_node(current)
        while current > 0 and self.heap_list[current] > self.heap_list[parent]:
            self.heap_list[current], self.heap_list[parent] = self.heap_list[parent], self.heap_list[current]
            current = parent
            parent = self.parent_node(current)

    def delete(self):
        print(self.top())
        self.heap_list[0] = self.heap_list[-1]
        self.heap_list.pop()
        self.heap_size -= 1
        current = 0
        left = self.left_child(current)
        right = self.right_child(current)
        while left < len(self.heap_list) or right < len(self.heap_list):
            max_index = current
            if left < self.heap_size and self.heap_list[max_index] < self.heap_list[left]:
                max_index = left
            if right < self.heap_size and self.heap_list[max_index] < self.heap_list[right]:
                max_index = right
            if max_index != current:
                self.heap_list[current], self.heap_list[max_index] = self.heap_list[max_index], self.heap_list[current]
                current = max_index
                left = self.left_child(current)
                right = self.right_child(current)
            else:
                break

    def upward(self, i):
        if i <= 0:
            return
        parent = self.parent_node(i)
        if self.heap_list[i] > self.heap_list[parent]:
            self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
            self.upward(parent)

    def insert_recursive(self, number):
        self.heap_list.append(number)
        self.heap_size += 1
        self.upward(self.heap_size - 1)

    def downwards(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        max_val = i
        if left < self.heap_size and self.heap_list[max_val] < self.heap_list[left]:
            max_val = left
        if right < self.heap_size and self.heap_list[max_val] < self.heap_list[right]:
            max_val = right
        if max_val != i:
            self.heap_list[i], self.heap_list[max_val] = self.heap_list[max_val], self.heap_list[i]
            self.downwards(max_val)

    def heapify(self, arr, i, size):
        left = self.left_child(i)
        right = self.right_child(i)
        max_val = i
        if left < size and arr[max_val] < arr[left]:
            max_val = left
        if right < size and arr[max_val] < arr[right]:
            max_val = right
        if max_val != i:
            arr[i], arr[max_val] = arr[max_val], arr[i]
            self.heapify(arr, max_val, size)

    def min_heapify(self, arr, i, size):
        left = self.left_child(i)
        right = self.right_child(i)
        min_val = i
        if left < size and arr[min_val] > arr[left]:
            min_val = left
        if right < size and arr[min_val] > arr[right]:
            min_val = right
        if min_val != i:
            arr[i], arr[min_val] = arr[min_val], arr[i]
            self.min_heapify(arr, min_val, size)

    def delete_recursive(self):
        print(self.top())
        self.heap_list[0] = self.heap_list[-1]
        self.heap_size -= 1
        self.heap_list.pop()
        self.downwards(0)

    def heap_sort(self, arr):
        size = len(arr)
        for i in range(len(arr)//2-1, -1, -1):
            self.heapify(arr, i, size)
        for i in range(len(arr)-1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            size -= 1
            self.heapify(arr, 0, i)

    def kth_largest(self, arr, k):
        arr_size = len(arr)
        for i in range(arr_size//2 - 1, -1, -1):
            self.min_heapify(arr, i, arr_size)
        print(arr)


if __name__ == "__main__":
    input_arr = [1, 4, 0, -1, 10, 11, 7, 55, 2]
    input_arr1 = [1, 4, 0, -1, 10, 11, 7, 55, 2]
    input_arr2 = [1, 4, 0, -1, 10, 11, 7, 55, 2]
    heap = Heap()
    # heap1 = Heap()
    # for num in input_arr:
    #     heap1.insert_recursive(num)
        # heap1.print_heap()
    for num in input_arr1:
        heap.insert(num)
        # heap.print_heap()
    # heap.print_heap()
    # heap.print_heap()
    # for i in range(9):
    #     heap.delete()
    #     heap.print_heap()

    # for i in range(9):
    #     heap1.delete_recursive()
    #     heap1.print_heap()
    heap.heap_sort(input_arr2)
    # print(input_arr2)
    # Kth largest number
    arr = [1, 4, 0, -1, 10, 11, 7, 55, 2]
    # arr1 = [1, 4, 0, -1, 10, 11, 7, 55, 2]
    # heapq.heapify(arr1)
    # print(arr1[0])
    # heapq.heappop(arr1);heapq.heappop(arr1)
    # print(arr1)
    k = 3  # int(input())
    heap.kth_largest(arr, k)
