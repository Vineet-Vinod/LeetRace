from bisect import bisect_left


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(pattern):
            pi = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j
            answer = []
            j = 0
            for i, c in enumerate(s):
                while j and c != pattern[j]:
                    j = pi[j - 1]
                if c == pattern[j]:
                    j += 1
                if j == len(pattern):
                    answer.append(i - j + 1)
                    j = pi[j - 1]
            return answer

        first, second = occurrences(a), occurrences(b)
        result = []
        for i in first:
            j = bisect_left(second, i - k)
            if j < len(second) and second[j] <= i + k:
                result.append(i)
        return result
