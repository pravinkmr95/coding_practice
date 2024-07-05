dp = [[-1 for _ in range(10)] for _ in range(10)]


def knapsack_rec(wt, val, W, n):
    if W == 0 or n == 0:
        return 0
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack_rec(wt, val, W - wt[n-1], n-1), knapsack_rec(wt, val, W, n-1))
    else:
        return knapsack_rec(wt, val, W, n-1)


def knapsack_memo(wt, val, W, n):
    if W == 0 or n == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    if wt[n-1] <= W:
        dp[n][W] = max(val[n-1] + knapsack_memo(wt, val, W - wt[n-1], n-1), knapsack_memo(wt, val, W, n-1))
        return dp[n][W]
    else:
        dp[n][W] = knapsack_memo(wt, val, W, n-1)
        return dp[n][W]


if __name__ == "__main__":
    value = [1, 2, 3]
    weight = [4, 5, 1]
    W = 4
    n = 3
    print(knapsack_rec(weight, value, W, n))
    print(knapsack_memo(weight, value, W, n))
