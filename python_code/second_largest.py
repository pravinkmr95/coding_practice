import sys


def second_largest(arr):
    first = arr[0]
    second = -sys.maxsize
    for i in range(1, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    print(second)


if __name__ == "__main__":
    a = [10, 5, 10]
    second_largest(a)
