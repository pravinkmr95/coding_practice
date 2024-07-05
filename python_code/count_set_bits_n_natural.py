def find_closest_power_of_2(n):
    x = 0
    while (1 << x) <= n:
        x += 1
    return x - 1


def count_set_bits(n):
    if n <= 1:
        return n

    # print("n === {}".format(n))
    x = find_closest_power_of_2(n)
    # print("x === {}".format(x))

    tpx = x * (1 << (x-1))
    # print("tpx === {}".format(tpx))
    y = n - (1 << x) + 1
    # print("y === {}".format(y))
    rest = n - (1 << x)
    # print("rest == {}".format(rest))
    ans = tpx + y + count_set_bits(rest)
    # print("ans == {}".format(ans))
    return ans


if __name__ == "__main__":
    # number = int(input())
    # print(count_set_bits(2))
    for i in range(21):
        print("n == {}, and 1's count == {}".format(i, count_set_bits(i)))
