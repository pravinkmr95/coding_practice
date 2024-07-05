def move_negatives_to_front(arr, size):
    j = 0
    for i in range(size):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


if __name__ == "__main__":
    input_arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    move_negatives_to_front(input_arr, len(input_arr))
    print(input_arr)
