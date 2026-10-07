class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        found = []
        for start in range(len(text)):
            for word in words:
                end = start + len(word)
                if text.startswith(word, start):
                    found.append([start, end - 1])
        return sorted(found)
