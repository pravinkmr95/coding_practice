def sort_arr(arr):
    right = len(arr) - 1
    mid = left = 0
    while mid <= right:
        if arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid]
            mid += 1
            left += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1


if __name__ == "__main__":
    input_arr = [1, 0, 2, 1, 0, 0, 1, 1, 2, 1, 2]
    input_arr = [1, 0]
    input_arr = [1, 0, 2]
    sort_arr(input_arr)
    print(input_arr)
