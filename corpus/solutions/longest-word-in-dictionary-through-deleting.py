class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word: str) -> bool:
            index = 0
            for char in s:
                if index < len(word) and word[index] == char:
                    index += 1
            return index == len(word)

        valid = [word for word in dictionary if is_subsequence(word)]
        return min(valid, key=lambda word: (-len(word), word), default="")
