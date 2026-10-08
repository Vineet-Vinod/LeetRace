class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[: len(s1)])
        if window == need:
            return True
        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1
            outgoing = s2[right - len(s1)]
            window[outgoing] -= 1
            if window[outgoing] == 0:
                del window[outgoing]
            if window == need:
                return True
        return False
