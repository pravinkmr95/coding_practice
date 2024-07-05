def find_largest_sum(arr):
    n = len(arr)
    max_ending_here = arr[0]
    max_so_far = arr[0]
    start = end = s = 0
    for i in range(1, n):
        max_ending_here += arr[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i
            print(start, end)
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
            # print(start, end)
    print(arr[start:end+1])
    return max_so_far


def find_largest_sum_dp(arr):
    result = arr[0]
    n = len(arr)
    for i in range(1, n):
        arr[i] = max(arr[i], arr[i] + arr[i-1])
        result = max(result, arr[i])
    return result


if __name__ == "__main__":
    input_arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    # input_arr = [-2, -3, -4, -1, -2, 1, -5, -3]
    # input_arr = [2, -3, -4, -1, -2, -1, -5, -3]
    print(find_largest_sum(input_arr))
    print(find_largest_sum_dp(input_arr))
