class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def stretchy(word: str) -> bool:
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False
                i_start, j_start = i, j
                while i < len(s) and s[i] == s[i_start]:
                    i += 1
                while j < len(word) and word[j] == word[j_start]:
                    j += 1
                source_count, word_count = i - i_start, j - j_start
                if word_count > source_count or (
                    source_count < 3 and source_count != word_count
                ):
                    return False
            return i == len(s) and j == len(word)

        return sum(stretchy(word) for word in words)
