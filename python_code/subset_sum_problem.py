def subset_sum_recu(arr, n, W):
    if W == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] <= W:
        return subset_sum_recu(arr, n-1, W-arr[n-1]) or subset_sum_recu(arr, n-1, W)
    else:
        return subset_sum_recu(arr, n-1, W)


def subset_sum_dp(arr, n, W):
    dp = [[False for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, W+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]


if __name__ == "__main__":
    input_arr = [3, 34, 4, 12, 5, 2]
    req_sum = 13
    num = len(input_arr)
    print(subset_sum_recu(input_arr, num, req_sum))
    print(subset_sum_dp(input_arr, num, req_sum))
