def find_missing_and_duplicate(arr):
    xor = 0
    for num in arr:
        xor = xor ^ num
    for num in range(len(arr) + 1):
        xor = xor ^ num
    rmsbm = xor & -xor
    x = 0
    y = 0
    for num in arr:
        if rmsbm & num == 0:
            x = x ^ num
        else:
            y = y ^ num
    for num in range(len(arr) + 1):
        if rmsbm & num == 0:
            x = x ^ num
        else:
            y = y ^ num
    if x in arr:
        print("repeating number = ", x)
        print("missing number = ", y)
    else:
        print("repeating number = ", y)
        print("missing number = ", x)


if __name__ == "__main__":
    input_arr = [3, 1, 3]
    input_arr1 = [4, 3, 6, 2, 1, 1]
    find_missing_and_duplicate(input_arr1)
