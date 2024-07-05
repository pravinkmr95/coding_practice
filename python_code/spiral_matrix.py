def spiral(arr, rows, columns):
    left = 0
    right = columns - 1
    top = 0
    bottom = rows - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            print(arr[top][i], end=" ")
        top += 1
        for i in range(top, bottom + 1):
            print(arr[i][right], end=" ")
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, - 1):
                print(arr[bottom][i], end=" ")
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, - 1):
                print(arr[i][left], end=" ")
            left += 1
        # print("")
        # print(top, bottom, left, right)
        # break


if __name__ == "__main__":
    inp = [[1, 2, 3, 4, 100],
           [5, 6, 7, 8, 200],
           [9, 10, 11, 12, 300],
           [13, 14, 15, 16, 400]]
    inp = [[1, 2],
           [5, 6],
           [9, 10],
           [13, 14]]
    inp = [[1],
           [2]
           ]
    inp = [[1],
           [2],
           [3]]
    row = len(inp)
    column = len(inp[0])
    spiral(inp, row, column)
