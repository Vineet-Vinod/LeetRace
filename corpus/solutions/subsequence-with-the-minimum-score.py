class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n = len(t)
        suffix = [len(s)] * (n + 1)
        j = n - 1
        for i in range(len(s) - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                suffix[j] = i
                j -= 1
        right = j + 1
        answer = right
        matched = 0
        for i, char in enumerate(s):
            if matched < n and char == t[matched]:
                matched += 1
                right = max(right, matched)
                while right < n and suffix[right] <= i:
                    right += 1
                answer = min(answer, right - matched)
        return answer
