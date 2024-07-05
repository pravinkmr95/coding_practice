from typing import List


class LetterCombination:
    def __init__(self):
        self.number_dict = {}

    def backtrack(self, digits, start, current_res):
        if start >= len(digits):
            self.output.append("".join(current_res))
            return
        for ch in self.number_dict[digits[start]]:
            current_res.append(ch)
            self.backtrack(digits, start+1, current_res)
            current_res.pop()
        return []

    def letter_combinations(self, digits: str) -> List[str]:
        self.number_dict = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        self.output = []
        self.backtrack(digits, 0, [])
        return self.output


if __name__ == "__main__":
    input_str = input()
    lc = LetterCombination()
    print(lc.letter_combinations(input_str))
