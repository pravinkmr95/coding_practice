def first_occurrence(arr, left, right, num):
    if left <= right:
        mid = (left + right)//2
        if arr[mid] == num and (mid == 0 or arr[mid-1] < arr[mid]):
            return mid
        elif arr[mid] < num:
            return first_occurrence(arr, mid+1, right, num)
        else:
            return first_occurrence(arr, left, mid-1, num)
    else:
        return -1


def last_occurrence(arr, left, right, num):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == num and (mid == len(arr)-1 or arr[mid + 1] > arr[mid]):
            return mid
        elif arr[mid] <= num:
            return last_occurrence(arr, mid + 1, right, num)
        else:
            return last_occurrence(arr, left, mid - 1, num)
    else:
        return -1


def find_occurrences(arr, num):
    n = len(arr)
    first = first_occurrence(arr, 0, n-1, num)
    # print("first==", first)
    last = last_occurrence(arr, 0, n-1, num)
    # print("last===", last)
    if first == -1 or last == -1:
        return -1
    else:
        return last - first + 1


if __name__ == "__main__":
    input_arr = [1, 1, 2, 2, 2, 2, 3]
    # input_arr = [1, 2, 2, 2, 2, 4, 4]
    x = 2
    print(find_occurrences(input_arr, x))
