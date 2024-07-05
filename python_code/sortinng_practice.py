import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        smallest_index = i
        for j in range(i+1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i-1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


def find_pivot_index(arr, left, right):
    random_index = random.randint(left, right)
    arr[right], arr[random_index] = arr[random_index], arr[right]
    pivot_val = arr[right]
    # print(pivot_val)
    j = left
    for i in range(left, right):
        if arr[i] < pivot_val:
            # print("i == {}, j == {}".format(i, j))
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[right] = pivot_val, arr[j]
    return j


def quick_sort(arr, left, right):
    if left < right:
        pi = find_pivot_index(arr, left, right)
        quick_sort(arr, left, pi-1)
        quick_sort(arr, pi+1, right)


def sorted_merge(arr, temp, l1, r1, l2, r2):
    while l1 <= r1 and l2 <= r2:
        if arr[l1] <= arr[l2]:
            temp.append(arr[l1])
            l1 += 1
        else:
            temp.append(arr[l2])
            l2 += 1
    while l1 <= r1:
        temp.append(arr[l1])
        l1 += 1
    while l2 <= r2:
        temp.append(arr[l2])
        l2 += 1


def merge(arr, left, mid, right):
    pass


def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right-left)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


if __name__ == "__main__":
    input_arr = [3, 1, 0, 8, 22, 12, 55, 0]
    input_arr1 = [2, 2, 2]
    input_arr2 = [3, 2, 1]
    # bubble_sort(input_arr)
    # selection_sort(input_arr)
    # insertion_sort(input_arr1)
    # print(find_pivot_index(input_arr, 0, len(input_arr)-1))
    # quick_sort(input_arr, 0, len(input_arr)-1)
    # temp = []
    # arr = [1, 4, 10, 12, 14, 55, 2, 3, 7]
    # merge(arr, temp, 0, 5, 6, 8)
    # print(temp)
    merge_sort(input_arr, 0, len(input_arr)-1)
    print(input_arr)

