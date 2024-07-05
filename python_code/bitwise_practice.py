def left_shift(number):
    print("shifting left")
    for i in range(1, 4):
        number = number << i
        print(number)


def right_shift(number):
    print("shifting right")
    while number:
        number = number >> 1
        print(number)


def print_binary(number):
    print("builtin:", bin(number)[2:])
    output = ""
    while number:
        if number & 1:
            output = "1" + output
        else:
            output = "0" + output
        number = number >> 1
    print(output)


def check_set_bits(number):
    for i in range(0, 32):
        if number & 1 << i:
            print(i)


def add_binary_strings(str1, str2):
    output = ""
    len1 = len(str1)
    len2 = len(str2)
    length = len1
    if len1 < len2:
        str1 = '0' * (len2 - len1) + str1
        length = len2
    elif len1 > len2:
        str2 = '0' * (len1 - len2) + str2
    carry = 0
    for i in range(length-1, -1, -1):
        first = int(str1[i])
        second = int(str2[i])
        digit = first ^ second ^ carry
        output = str(digit) + output
        carry = (first & second) | second & carry | first & carry
    if carry:
        output = '1' + output
    return output


if __name__ == "__main__":
    # x = int(input())
    # left_shift(x)
    # right_shift(x)
    # print_binary(x)
    # check_set_bits(x)
    print(add_binary_strings("101", "1000110"))
    print(add_binary_strings("111", "111"))
