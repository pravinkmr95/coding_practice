output_arr = [[-1 for _ in range(60)] for _ in range(60)]


def max_profit_using_knapsack_rec(N, W, profits, wt):
    if N == 0 or W == 0:
        return 0
    if wt[N-1] <= W:
        return max(profits[N-1] + max_profit_using_knapsack_rec(N-1, W - wt[N-1], profits, wt),
                   max_profit_using_knapsack_rec(N-1, W, profits, wt))
    else:
        return max_profit_using_knapsack_rec(N-1, W, profits, wt)


def max_profit_using_knapsack_memo(N, W, profits, wt):
    if N == 0 or W == 0:
        return 0
    if output_arr[N][W] != -1:
        return output_arr[N][W]
    if wt[N-1] <= W:
        output_arr[N][W] = max(profits[N-1] + max_profit_using_knapsack_memo(N-1, W-wt[N-1], profits, wt),
                               max_profit_using_knapsack_memo(N-1, W, profits, wt))
        return output_arr[N][W]
    else:
        output_arr[N][W] = max_profit_using_knapsack_memo(N-1, W, profits, wt)
        return output_arr[N][W]


def max_profit_using_knapsack_dp(N, W, profits, wt):
    # dp1 = [[0]*(W+1)]*(N+1)
    # dp = dp2 = [[0 for x in range(W + 1)] for x in range(N + 1)]
    # print(dp1 == dp2)
    # dp = [[0]*(W+1)]*(N+1)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for p in range(1, N+1):
        for k in range(1, W+1):
            if wt[p-1] <= k:
                dp[p][k] = max(profits[p-1] + dp[p-1][k - wt[p-1]],
                               dp[p-1][k])
            else:
                dp[p][k] = dp[p-1][k]
    return dp[N][W]


def add_num_list(arr, num, index, size):
    if size < index:
        print("outbound")
        return
    if size == 0 or index == size:
        arr.append(num)
        return
    last = arr[-1]
    for i in range(size-1, index-1, -1):
        arr[i] = arr[i-1]
    arr.append(last)
    arr[index] = num
    return


def find_number(arr, num):
    for index, number in enumerate(arr):
        if number == num:
            return index
    return -1


def delete_arr_num(arr, num):
    pos = find_number(arr, num)
    if pos != -1:
        for i in range(pos, len(arr)-1):
            arr[i] = arr[i+1]
        arr.pop()


def subset_sum_dp(input_arr, N, W):
    dp = [[False for i in range(W+1)] for j in range(N+1)]
    for i in range(N+1):
        for j in range(W+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    # for i in range(N+1):
    #     print(dp[i][0])
    # for j in range(W+1):
    #     print(dp[0][j])

    for i in range(1, N+1):
        for j in range(1, W+1):
            if input_arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-input_arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][W]


def equal_subset_sum_dp(input_arr, N):
    total_sum = 0
    for num in input_arr:
        total_sum += num
    if total_sum % 2 == 0:
        return subset_sum_dp(input_arr, N, total_sum//2)
    else:
        return False


def subsets_with_given_sum_dp(input_arr, N, W):
    dp = [[0 for i in range(W + 1)] for j in range(N + 1)]
    for i in range(N + 1):
        for j in range(W + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if input_arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - input_arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[N][W]


if __name__ == "__main__":
    profits1 = [1, 2, 3]
    wt1 = [4, 5, 1]
    profits2 = [60, 100, 120]
    wt2 = [10, 20, 30]
    N1 = len(profits1)
    N2 = len(profits2)
    W1 = 4
    W2 = 50
    # print(max_profit_using_knapsack_rec(N1, W1, profits1, wt1))
    # print(max_profit_using_knapsack_rec(N2, W2, profits2, wt2))
    profits3 = [1, 2, 3]
    wt3 = [4, 5, 6]
    N3 = len(profits3)
    W3 = 3
    # print(max_profit_using_knapsack_rec(N3, W3, profits3, wt3))
    # print(max_profit_using_knapsack_memo(N2, W2, profits2, wt2))
    # print(max_profit_using_knapsack_dp(N2, W2, profits2, wt2))
    # insert_arr = [1, 2, 3, 4, 5, 6]
    # # insert_arr = [1,2]
    # insert_arr = [1]
    # print(insert_arr)
    # # add_num_list(insert_arr, 55, 1, len(insert_arr))
    # delete_arr_num(insert_arr, 1)
    # print(insert_arr)
    # sub_arr = [2, 3, 7, 8, 10]
    # sub_arr = [2, 5, 7, 8, 10]
    sub_arr = [2, 3, 7, 8, 10, 11]
    sub_arr = [1, 2, 3, 3]
    total_sum = 6
    # print(subset_sum_dp(sub_arr, len(sub_arr), total_sum))
    # sub_arr = [1, 5, 11, 5]
    # print(equal_subset_sum_dp(sub_arr, len(sub_arr)))
    print(subsets_with_given_sum_dp(sub_arr, len(sub_arr), total_sum))
