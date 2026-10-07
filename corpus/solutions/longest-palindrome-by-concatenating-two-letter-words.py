class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)
        length = 0
        center = False
        for word in list(counts):
            reverse = word[::-1]
            if word == reverse:
                pairs = counts[word] // 2
                length += pairs * 4
                if counts[word] % 2:
                    center = True
            elif word < reverse:
                length += min(counts[word], counts[reverse]) * 4
        return length + (2 if center else 0)
