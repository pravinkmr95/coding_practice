def find_peak_element_n(arr):
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[n-1] >= arr[n-2]:
        return n-1
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i
    return -1


def find_peak_element_binary(arr, left, right):
    if left <= right:
        mid = left + (right - left)//2
        if mid == 0 and arr[mid] >= arr[mid+1]:
            return mid
        elif mid == len(arr)-1 and arr[mid] >= arr[mid-1]:
            return mid
        elif arr[mid] >= arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] < arr[mid-1]:
            return find_peak_element_binary(arr, left, mid-1)
        else:
            return find_peak_element_binary(arr, mid+1, right)


if __name__ == "__main__":
    input_arr1 = [5, 10, 20, 15]
    input_arr = [10, 20, 15, 2, 23, 90, 67]
    input_arr2 = [2, 2, 2, 2]
    input_arr3 = [1, 3, 20, 4, 1, 0]
    # print(find_peak_element_n(input_arr3))
    x = find_peak_element_binary(input_arr3, 0, len(input_arr3)-1)
    print(x)
