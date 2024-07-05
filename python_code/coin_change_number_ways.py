def max_number_ways(arr, n, W):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(W+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]


if __name__ == "__main__":
    coins = [2, 5, 3, 6]
    summ = 10 #5
    coins = [1, 2, 3]
    summ = 4 #4
    n = len(coins)
    print(max_number_ways(coins, n, summ))
