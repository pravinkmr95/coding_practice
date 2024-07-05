from collections import defaultdict


if __name__ == "__main__":
    string = "ababbababbb"
    window_size = 4
    output = []
    char_dict = defaultdict(lambda: 0)
    start = 0
    for i in range(len(string)):
        char = string[i]
        char_dict[char] += 1
        if i >= window_size-1:
            output.append(len(char_dict))
            if string[start] in char_dict and char_dict[string[start]] > 1:
                char_dict[string[start]] -= 1
            else:
                char_dict.pop(string[start])
            start += 1
    print(output)

