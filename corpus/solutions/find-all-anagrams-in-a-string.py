class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        target = Counter(p)
        window = Counter(s[: len(p)])
        answer = []
        for start in range(len(s) - len(p) + 1):
            if window == target:
                answer.append(start)
            if start + len(p) < len(s):
                outgoing = s[start]
                window[outgoing] -= 1
                if window[outgoing] == 0:
                    del window[outgoing]
                window[s[start + len(p)]] += 1
        return answer
