def find_max_water(arr):
    n = len(arr)
    left = [0] * n
    left[0] = arr[0]
    right = [0] * n
    right[n-1] = arr[n-1]
    for i in range(1, n):
        left[i] = max(arr[i], left[i-1])

    for i in range(n-2, -1, -1):
        right[i] = max(arr[i], right[i+1])

    ts = 0
    for i in range(1, n-1):
        ts += min(left[i], right[i]) - arr[i]
    return ts


if __name__ == "__main__":
    input_arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] #6
    input_arr1 = [4, 2, 0, 3, 2, 5] #9
    print(find_max_water(input_arr1))
