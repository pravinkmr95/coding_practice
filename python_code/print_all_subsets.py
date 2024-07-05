def print_all_subsets_bitwise(string_val, str_len):
    output = []
    for num in range(1 << str_len):
        subset = ""
        for i in range(str_len):
            if num & 1 == 1:
                subset += string_val[i]
            num = num >> 1
        output.append(subset)
    print(output)


def print_all_subsets_recursion(input_string, output_string):
    if len(input_string) == 0:
        print(output_string)
        return
    output1 = output_string
    output2 = output_string + input_string[0]
    input_string = input_string[1:]
    print_all_subsets_recursion(input_string, output1)
    print_all_subsets_recursion(input_string, output2)
    return


if __name__ == "__main__":
    input_str = "abc"
    n = len(input_str)
    print_all_subsets_bitwise(input_str, n)
    # print_all_subsets_recursion(input_str, "")
