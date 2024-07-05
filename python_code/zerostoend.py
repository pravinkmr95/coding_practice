def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


if __name__ == "__main__":
    input_list = [1, 2, 0, 4, 3, 0, 5, 0]
    input_list2 = [1, 2, 0, 0, 0, 3, 6]
    move_zeros(input_list2)
    print(input_list2)
