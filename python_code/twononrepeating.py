def find_non_repeating_number(array):
    xor = 0
    for num in array:
        xor = xor ^ num
    rmsbm = xor & -xor
    x = 0
    y = 0
    for num in array:
        if num & rmsbm == 0:
            x = x ^ num
        else:
            y = y ^ num
    print("Numbers are " + str(x) + " and " + str(y))


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 5, 7, 6, 3, 8, 8]
    find_non_repeating_number(arr)
