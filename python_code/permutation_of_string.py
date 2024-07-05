def permute(string, left, right, output):
    if left == right:
        output.append("".join(string))
        return
    s1 = set()
    for i in range(left, right+1):
        if string[i] not in s1:
            s1.add(string[i])
            string[left], string[i] = string[i], string[left]
            permute(string, left+1, right, output)
            string[left], string[i] = string[i], string[left]


if __name__ == "__main__":
    input_str = list("AAC")
    output = []
    permute(input_str, 0, len(input_str)-1, output)
    print(output)
