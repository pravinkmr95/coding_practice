def minimum_number_of_platform_required(arr, dep, n):
    arr.sort()
    dep.sort()
    max_platform = 0
    count = 0
    i = 0
    j = 0
    while i < n:
        if arr[i] <= dep[j]:
            count += 1
            max_platform = max(count, max_platform)
            i += 1
        else:
            count -= 1
            j += 1
    return max_platform


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = len(arr)
    print(minimum_number_of_platform_required(arr, dep, n))
# 1 1 2 2 3 7
# 1 2 2 2 3 7    1 move
# 1 2 3 2 3 7    1 move
# 1 2 3 4 3 7    2 move
# 1 2 3 4 3 7    2 move
