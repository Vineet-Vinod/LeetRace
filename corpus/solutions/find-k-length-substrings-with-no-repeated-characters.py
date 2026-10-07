class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        counts = Counter()
        duplicates = 0
        answer = 0
        for index, char in enumerate(s):
            counts[char] += 1
            if counts[char] == 2:
                duplicates += 1
            if index >= k:
                outgoing = s[index - k]
                if counts[outgoing] == 2:
                    duplicates -= 1
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]
            if index >= k - 1 and duplicates == 0:
                answer += 1
        return answer
