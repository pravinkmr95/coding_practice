def print_one_to_n(num):
    if num < 1:
        return
    print_one_to_n(num - 1)
    print(num)


def print_n_to_one(num):
    if num < 1:
        return
    print(num)
    print_n_to_one(num - 1)


def get_factorial(num):
    if num == 1:
        return 1
    return num * get_factorial(num-1)


if __name__ == "__main__":
    x = int(input())
    # print_one_to_n(x)
    # print_n_to_one(x)
    fact = get_factorial(x)
    print(fact)
