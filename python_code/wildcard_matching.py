def matching_pattern_rec(string, pattern, m, n):
    if m == 0 and n == 0:
        return True
    if n == 0 and m != 0:
        return False
    if m == 0 and n != 0:
        for k in range(n):
            if pattern[k] != "*":
                return False
        return True
    if string[m-1] == pattern[n-1] or pattern[n-1] == '?':
        return matching_pattern_rec(string, pattern, m-1, n-1)
    elif pattern[n-1] == "*":
        return (matching_pattern_rec(string, pattern, m-1, n)
                or matching_pattern_rec(string, pattern, m, n-1))
    else:
        return False


if __name__ == "__main__":
    string = "baaabab"
    pattern = "*****ba*****ab"
    pattern = "ba*****ab"
    pattern = "ba*ab"
    # char pattern[] = "a*ab"
    # char pattern[] = "a*****ab"
    # char pattern[] = "*a*****ab"
    # char pattern[] = "ba*ab****"
    # char pattern[] = "****"
    pattern = "*"
    pattern = "aa?ab"
    # char pattern[] = "b*b"
    # char pattern[] = "a*a"
    # char pattern[] = "baaabab"
    # char pattern[] = "?baaabab"
    # char pattern[] = "*baaaba*"
    print(matching_pattern_rec(string, pattern, len(string), len(pattern)))
