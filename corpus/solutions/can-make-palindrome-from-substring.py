class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for char in s:
            prefix.append(prefix[-1] ^ (1 << (ord(char) - ord("a"))))
        return [
            ((prefix[right + 1] ^ prefix[left]).bit_count() // 2) <= replacements
            for left, right, replacements in queries
        ]
