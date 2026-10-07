class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        found = set()
        n = len(text)
        for size in range(1, n // 2 + 1):
            equal = 0
            for i in range(n - size):
                equal = equal + 1 if text[i] == text[i + size] else 0
                if equal >= size:
                    found.add(text[i - size + 1 : i + 1])
        return len(found)
