class Solution:
    def longestAwesome(self, s: str) -> int:
        first = {0: -1}
        mask = 0
        answer = 0
        for index, digit in enumerate(s):
            mask ^= 1 << int(digit)
            answer = max(answer, index - first.get(mask, index))
            for bit in range(10):
                answer = max(answer, index - first.get(mask ^ (1 << bit), index))
            first.setdefault(mask, index)
        return answer
