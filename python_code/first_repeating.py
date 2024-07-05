def find_first_repeating_with_less_i(arr):
    numbers = {}
    min_index_rep = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in numbers:
            min_index_rep = arr[i]
        else:
            numbers[arr[i]] = 1
    return min_index_rep


if __name__ == "__main__":
    inp = [10, 5, 3, 4, 3, 5, 6]
    inp1 = [6, 10, 5, 4, 9, 120, 4, 6, 10]
    print(find_first_repeating_with_less_i(inp))
