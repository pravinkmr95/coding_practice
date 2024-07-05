def are_anagram(string1, string2):
    n1 = len(string1)
    n2 = len(string2)
    if n1 != n2:
        return False
    list1 = [0] * 26
    list2 = [0] * 26
    for char in string1:
        list1[ord(char) - ord('a')] += 1
    for char in string2:
        list2[ord(char) - ord('a')] += 1
    print(list1)
    print(list2)

    return True if tuple(list1) == tuple(list2) else False


if __name__ == "__main__":
    s1 = "gram"
    s2 = "armq"
    print(are_anagram(s1, s2))
