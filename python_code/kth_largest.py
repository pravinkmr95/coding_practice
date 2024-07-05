class kth_largest:
    def __init__(self):
        self.heap_list = []
        self.heap_size = 0

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def upward(self, i):
        if i <= 0:
            return
        parent = self.parent(i)
        if self.heap_list[i] < self.heap_list[parent]:
            self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
            self.upward(parent)

    def insert(self, number):
        self.heap_list.append(number)
        self.heap_size += 1
        self.upward(self.heap_size - 1)

    def downward(self, i):
        minimum = i
        left = self.left(i)
        right = self.right(i)
        if left < self.heap_size and self.heap_list[left] < self.heap_list[minimum]:
            minimum = left
        if right < self.heap_size and self.heap_list[right] < self.heap_list[minimum]:
            minimum = right
        if minimum != i:
            self.heap_list[i], self.heap_list[minimum] = self.heap_list[minimum], self.heap_list[i]
            self.downward(minimum)

    def pop(self):
        self.heap_list[0] = self.heap_list[-1]
        self.heap_list.pop()
        self.heap_size -= 1
        self.downward(0)

    def top(self):
        return self.heap_list[0]

    def print_heap(self):
        print(self.heap_list)

    def find_kth_largest(self, arr, k):
        for num in arr:
            self.insert(num)
            if self.heap_size > k:
                self.pop()
        self.print_heap()
        return self.top()


if __name__ == "__main__":
    arr = [1, 4, 0, -1, 10, 11, 7, 55, 2]
    obj = kth_largest()
    k = int(input())
    print(obj.find_kth_largest(arr, k))
    # for i in range(len(arr)):
    #     k = int(input())
    #     print(obj.find_kth_largest(arr, k))

