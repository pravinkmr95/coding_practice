def merge(arr, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid

    left_arr = [0] * left_size
    right_arr = [0] * right_size
    for i in range(left_size):
        left_arr[i] = arr[left + i]
    for j in range(right_size):
        right_arr[j] = arr[mid + 1 + j]
    # print("left_arr", left_arr)
    # print("right_arr", right_arr)

    i = j = 0
    k = left
    while i < left_size and j < right_size:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < left_size:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < right_size:
        arr[k] = right_arr[j]
        k += 1
        j += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


if __name__ == "__main__":
    input_arr = [0, 1, 4, 2, 9, 1, 3, 7, 10, -1, 22]
    merge_sort(input_arr, 0, len(input_arr)-1)
    # input_arr = [1, 3, 4, 0, 2]
    # mid = (len(input_arr)-1)//2
    # merge(input_arr, 0, mid, len(input_arr)-1)
    print(input_arr)
