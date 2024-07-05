def word_break(string, words, start):
    if start >= len(string):
        return True
    i = start + 1
    while i <= len(string):
        if string[start:i] in words and word_break(string, words, i):
            return True
        i += 1
    return False


def word_break_rec(string, words):
    dictionary = set(words)
    return word_break(string, dictionary, 0)


def wordBreak(s, words):
    dictionary = set(words)
    n = len(s)
    dp = [False for _ in range(n+1)]
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                break
    print(dp)
    return dp[n]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]

    s = "applepenapple"
    wordDict = ["apple", "pen"]

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    # s = "a"
    # wordDict = ["a"]
    print(wordBreak(s, wordDict))
