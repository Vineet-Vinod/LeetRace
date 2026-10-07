class Solution:
    def partition(self, s: str) -> List[List[str]]:
        size = len(s)
        palindrome = [[False] * size for _ in range(size)]
        for end in range(size):
            for start in range(end + 1):
                palindrome[start][end] = s[start] == s[end] and (
                    end - start < 2 or palindrome[start + 1][end - 1]
                )
        partitions = []

        def build(start: int, chosen: List[str]) -> None:
            if start == size:
                partitions.append(chosen.copy())
                return
            for end in range(start, size):
                if palindrome[start][end]:
                    chosen.append(s[start : end + 1])
                    build(end + 1, chosen)
                    chosen.pop()

        build(0, [])
        partitions.sort()
        return partitions
