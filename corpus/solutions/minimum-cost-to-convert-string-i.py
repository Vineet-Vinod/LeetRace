class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        infinity = 10**18
        distance = [[infinity] * 26 for _ in range(26)]
        for letter in range(26):
            distance[letter][letter] = 0
        for first, second, price in zip(original, changed, cost):
            start, end = ord(first) - ord("a"), ord(second) - ord("a")
            distance[start][end] = min(distance[start][end], price)
        for middle in range(26):
            for start in range(26):
                if distance[start][middle] == infinity:
                    continue
                for end in range(26):
                    distance[start][end] = min(
                        distance[start][end],
                        distance[start][middle] + distance[middle][end],
                    )
        total = 0
        for first, second in zip(source, target):
            value = distance[ord(first) - ord("a")][ord(second) - ord("a")]
            if value == infinity:
                return -1
            total += value
        return total
