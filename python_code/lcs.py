def lcs_dp(s1, s2, x, y):
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    for i in range(1, x+1):
        for j in range(1, y+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[x][y]


def lcs(s1, s2, x, y):
    if x == 0 or y == 0:
        return 0
    if s1[x-1] == s2[y-1]:
        return 1 + lcs(s1, s2, x-1, y-1)
    else:
        return max(lcs(s1, s2, x-1, y), lcs(s1, s2, x, y-1))


if __name__ == "__main__":
    s1 = "abcsfg"
    s2 = "nabcsfk"
    print(lcs_dp(s1, s2, len(s1), len(s2)))

