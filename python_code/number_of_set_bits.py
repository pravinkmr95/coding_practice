def number_of_set_bits(x):
    count = 0
    while x > 0:
        rmsbm = x & -x
        x -= rmsbm
        count += 1
    return count


if __name__ == "__main__":
    number = input()
    number = int(number)
    print(number_of_set_bits(number))
