def binary_search(arr, left, right, key):
    if left > right:
        return
    mid = (left + right)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, mid+1, right, key)
    else:
        return binary_search(arr, left, mid-1, key)


if __name__ == "__main__":
    a = [2, 3, 4, 10, 40]
    key1 = 10
    print(binary_search(a, 0, len(a)-1, key1))
