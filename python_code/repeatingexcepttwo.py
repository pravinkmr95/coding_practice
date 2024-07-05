def two_non_repeated_numbers(arr):
    xxory = 0
    for num in arr:
        xxory = xxory ^ num
    rmsbv = xxory & -xxory
    x = 0
    y = 0
    for num in arr:
        if num & rmsbv == 0:
            x = x ^ num
        else:
            y = y ^ num
    print(x, " ", y)


if __name__ == "__main__":
    a = [1, 3, 5, 8, 1, 8, 3, 9]
    two_non_repeated_numbers(a)
