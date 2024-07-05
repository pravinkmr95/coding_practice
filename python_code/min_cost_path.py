import sys


def cost_path_dp(cost, m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = cost[0][0]
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + cost[0][j]

    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = cost[i][j] + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    return dp[m][n]


def cost_path(cost, m, n):
    if m < 0 or n < 0:
        return sys.maxsize
    if m == 0 and n == 0:
        return cost[m][n]
    else:
        return cost[m][n] + min(cost_path(cost, m-1, n-1), cost_path(cost, m, n-1),
                                cost_path(cost, m-1, n))


if __name__ == "__main__":
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    print(cost_path(cost, 2, 2))
    print(cost_path_dp(cost, 2, 2))
