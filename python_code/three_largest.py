import sys


def three_largest(array):
    first = array[0]
    second = -sys.maxsize
    third = -(sys.maxsize - 1)
    if len(array) < 3:
        print("-1")
        return
    for i in range(1, len(array)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]
    print(first, " , ", second, " , ", third)


if __name__ == "__main__":
    arr = [10, 4, 3, 50, 2, 90]
    three_largest(arr)
