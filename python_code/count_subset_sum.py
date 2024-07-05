def count_subsets(arr, n, W):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, W+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]


if __name__ == "__main__":
    input_arr = [1, 2, 3, 3]
    W = 6
    input_arr = [5, 2, 3, 10, 6, 8]
    W = 10
    input_arr = [2, 5, 1, 4, 3]
    W = 3
    input_arr = [5, 2, 3, 10, 6, 8]
    W = 10
    input_arr = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
    W = 31
    n = len(input_arr)
    print(count_subsets(input_arr, n, W))
