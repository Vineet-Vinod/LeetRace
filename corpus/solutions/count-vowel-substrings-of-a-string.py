class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        result = 0
        for start in range(len(word)):
            seen = set()
            for end in range(start, len(word)):
                if word[end] not in vowels:
                    break
                seen.add(word[end])
                result += len(seen) == 5
        return result
