from collections import defaultdict


def group_anagrams(string_list):
    dictionary = defaultdict(list)
    for string in string_list:
        char_list = [0] * 26
        for char in string:
            char_list[ord(char) - ord('a')] += 1
        dictionary[tuple(char_list)].append(string)
    return list(dictionary.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = [""]
    strs = ["a"]
    print(group_anagrams(strs))
