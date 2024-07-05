def max_profit(arr):
    n = len(arr)
    max_from_end = arr[-1]
    if n < 2:
        return 0
    max_profit_so_far = 0
    for i in range(n-2, -1, -1):
        if arr[i] < max_from_end:
            max_profit_so_far = max(max_profit_so_far, max_from_end-arr[i])
        if arr[i] > max_from_end:
            max_from_end = arr[i]
    return max_profit_so_far


if __name__ == "__main__":
    input_arr = [7, 1, 5, 3, 6, 4]
    input_arr = [7, 6, 4, 3, 1]
    input_arr = [1, 3, 4, 7, 6]
    print(max_profit(input_arr))
