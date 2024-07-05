import sys


def largest_three(input_arr):
    if len(input_arr) < 3:
        print("Invalid input")
        return
    first = second = third = -sys.maxsize
    for num in input_arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num

    print("first = {}".format(first))
    print("second = {}".format(second))
    print("third = {}".format(third))


def move_zeros_to_end(inp):
    i = 0
    for j in range(len(inp)):
        if inp[j] != 0:
            inp[j], inp[i] = inp[i], inp[j]
            i += 1
    print(inp)


def segregate_even_odd(input_arr):
    i = 0
    for j in range(len(input_arr)):
        if input_arr[j] % 2 == 0:
            input_arr[i], input_arr[j] = input_arr[j], input_arr[i]
            i += 1
    print(input_arr)


def binary_search(arr, left, right, number):
    if left <= right:
        mid = (left + right)//2
        if arr[mid] == number:
            return mid
        if arr[mid] > number:
             return binary_search(arr, left, mid-1, number)
        else:
            return binary_search(arr, mid+1, right, number)
    return -1


if __name__ == "__main__":
    arr = [10, 4, 3, 50, 23, 90]
    arr1 = [2, 2, 2]
    # largest_three(arr1)
    a1 = [1, 2, 0, 4, 3, 0, 5, 0]
    a2 = [1, 2, 0, 0, 0, 3, 6]
    a3 = [0, 0, 0, 0, 1]
    a4 = [0, 0, 0, 0, 0]
    a5 = [0, 1, 2, 3, 4, 5]
    a6 = [1, 2, 3]
    # move_zeros_to_end(a1)
    # move_zeros_to_end(a2)
    # move_zeros_to_end(a3)
    # move_zeros_to_end(a4)
    # move_zeros_to_end(a5)
    # move_zeros_to_end(a6)

    # seg = [7, 2, 9, 4, 6, 1, 3, 8, 5]
    # seg1 = [1, 3, 2, 4, 7, 6, 9, 10]
    # segregate_even_odd(seg1)
    numbers = [1, 4, 6, 8, 10, 22, 25, 30, 40, 60]
    for num in numbers:
        num = 55
        print(binary_search(numbers, 0, len(numbers) - 1, num))
        break
