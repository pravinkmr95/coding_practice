def sub_array_sub_positive(arr, x):
    # n = len(arr)
    # for i, num in enumerate(arr):
    #     curr_sum = num
    #     for j in range(i+1, n):
    #         if curr_sum == x:
    #             return i, j-1
    #         curr_sum += arr[j]
    current_sum = 0
    current_start = 0
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum == x:
            return current_start, i
        if current_sum > x:
            # print("while")
            # print("current_sum", current_sum)
            while current_sum >= x and current_start < i:
                current_sum -= arr[current_start]
                # print("current_sum", current_sum)
                current_start += 1
                if current_sum == x:
                    return current_start, i


def sub_array_sub_dp(arr, num):
    dp = {}
    n = len(arr)
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if current_sum == num:
            return 0, i
        if current_sum - num in dp:
            return dp[current_sum - num]+1, i
        dp[current_sum] = i


def count_sub_array_sum_x(arr, key):
    dp = {}
    curr_sum = 0
    result = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == key:
            result += 1
        if curr_sum - key in dp:
            result += dp[curr_sum - key]
        if curr_sum in dp:
            dp[curr_sum] += 1
        else:
            dp[curr_sum] = 1
    return result


def largest_sub_array_sum_x(arr, target):
    n = len(arr)
    dp = {}
    curr_sum = 0
    largest_size = 0
    for i in range(n):
        curr_sum += arr[i]
        # print("curr_sum", curr_sum)
        if curr_sum == target:
            print("curr_sum")
            # print(0, i)
            largest_size = i + 1
        if curr_sum - target in dp:
            # print(dp[curr_sum - target] + 1, i)
            length = i - dp[curr_sum - target]
            if length > largest_size:
                print(dp[curr_sum - target]+1, i)
                largest_size = length
        dp[curr_sum] = i
    return largest_size


def max_size_subarray_with_equal_0_1(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
    return largest_sub_array_sum_x(arr, 0)


if __name__ == "__main__":
    input_arr = [1, 4, 20, 3, 10, 5, 33]
    x = 33
    # input_arr = [15, 2, 4, 8, 9, 5, 10, 23]
    # x = 35
    input_arr = [10, 2, -2, -20, 10]
    x = -10
    input_arr = [3, 9, -2, 4, 1, -7, 2, 6, -5, 8, -3, -7, 6, 2, 1]
    x = 5
    # print(sub_array_sub_positive(input_arr, x))
    # print(sub_array_sub_dp(input_arr, x))
    # print(count_sub_array_sum_x(input_arr, x))
    # print(largest_sub_array_sum_x(input_arr, x))
    input_arr = [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1]
    print(max_size_subarray_with_equal_0_1(input_arr))
    print(input_arr[10:16])
