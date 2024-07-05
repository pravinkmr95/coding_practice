from collections import deque


def print_pattern(n: int, x: int):
    queue = deque()
    count = 0
    i = 0
    while i < n:
        if count < x:
            queue.append(count)
            count += 1
            i += 1
            continue
        count -= 1
        while i < n and count > 0:
            i += 1
            count -= 1
            queue.append(count)
        count += 1

    for i in range(n):
        k = queue.popleft()
        for j in range(x):
            if j == k:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def print_pattern(n: int, x: int):
    for i in range(n):
        for j in range(n):
            if j == (i % x) or j == (x - 1 - (i % x)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    xx = 5
    yy = 3
    print_pattern(xx, yy)
