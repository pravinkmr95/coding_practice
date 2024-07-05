def find_LIS(arr):
    n = len(arr)
    output = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                output[i] = max(output[i], output[j]+1)
    return max(output)


if __name__ == "__main__":
    input_arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(find_LIS(input_arr))