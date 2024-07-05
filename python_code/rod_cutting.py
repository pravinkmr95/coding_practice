def rod_cutting(price, length, N, W):
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if length[i-1] <= j:
                dp[i][j] = max(price[i-1] + dp[i][j-length[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][W]


if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20] # 22
    price = [3, 5, 8, 9, 10, 17, 17, 20] # 24
    length = [i for i in range(1, len(price)+1)]
    n = len(price)
    max_profit = rod_cutting(price, length, n, n)
    print(max_profit)
