class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = Counter()
        window = Counter()
        distinct = 0
        for index, char in enumerate(s):
            window[char] += 1
            if window[char] == 1:
                distinct += 1
            if index >= minSize:
                outgoing = s[index - minSize]
                window[outgoing] -= 1
                if window[outgoing] == 0:
                    distinct -= 1
                    del window[outgoing]
            if index >= minSize - 1 and distinct <= maxLetters:
                counts[s[index - minSize + 1 : index + 1]] += 1
        return max(counts.values(), default=0)
