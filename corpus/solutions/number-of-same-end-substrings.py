class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [[0] * 26]
        for char in s:
            counts = prefix[-1].copy()
            counts[ord(char) - ord("a")] += 1
            prefix.append(counts)
        answers = []
        for left, right in queries:
            total = 0
            for letter in range(26):
                count = prefix[right + 1][letter] - prefix[left][letter]
                total += count * (count + 1) // 2
            answers.append(total)
        return answers
