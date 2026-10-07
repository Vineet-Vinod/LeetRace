class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        frequencies = [0] * (1 << 10)
        frequencies[0] = 1
        mask = answer = 0
        for char in word:
            mask ^= 1 << (ord(char) - ord("a"))
            answer += frequencies[mask]
            for bit in range(10):
                answer += frequencies[mask ^ (1 << bit)]
            frequencies[mask] += 1
        return answer
