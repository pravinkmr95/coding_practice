from collections import deque
import pdb

add_x_y = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(grid, x, y):
    grid_rows = len(grid)
    grid_columns = len(grid[0])
    visited = [[False for _ in range(grid_columns)] for _ in range(grid_rows)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while len(queue) > 0:
        i, j = queue.popleft()
        print(grid[i][j], end=" ")
        for addx, addy in add_x_y:
            new_x = i + addx
            new_y = j + addy
            if 0 <= new_x < grid_rows and 0 <= new_y < grid_columns and visited[new_x][new_y] is False:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True


def dfs(grid, x, y):
    grid_rows = len(grid)
    grid_columns = len(grid[0])
    visited = [[False for _ in range(grid_columns)] for _ in range(grid_rows)]
    stack = [(x, y)]
    visited[x][y] = True
    while len(stack) > 0:
        if stack:
            i, j = stack.pop()
            print(grid[i][j], end=" ")
            # if grid[i][j] == 16:
            #     pdb.set_trace()
            for addx, addy in add_x_y:
                new_x = i + addx
                new_y = j + addy
                if 0 <= new_x < grid_rows and 0 <= new_y < grid_columns and visited[new_x][new_y] is False:
                    stack.append((new_x, new_y))
                    visited[new_x][new_y] = True


if __name__ == "__main__":
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    # bfs(grid, 2, 1)
    # print()
    dfs(grid, 2, 1)
