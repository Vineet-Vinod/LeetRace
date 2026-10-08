from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        parent = list(range(max(end for _, end in paint) + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        result = []
        for start, end in paint:
            count = 0
            x = find(start)
            while x < end:
                parent[x] = find(x + 1)
                count += 1
                x = parent[x]
            result.append(count)
        return result
