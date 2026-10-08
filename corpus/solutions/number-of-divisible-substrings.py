class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        groups = ("ab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz")
        value = {char: digit for digit, chars in enumerate(groups, 1) for char in chars}
        answer = 0
        for start in range(len(word)):
            total = 0
            for end in range(start, len(word)):
                total += value[word[end]]
                answer += total % (end - start + 1) == 0
        return answer
