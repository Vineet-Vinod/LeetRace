from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ordered = sorted(nums)
        children = [[-1, -1]]
        answer = [-1] * len(queries)
        cursor = 0
        for limit, value, index in sorted(
            (limit, value, i) for i, (value, limit) in enumerate(queries)
        ):
            while cursor < len(ordered) and ordered[cursor] <= limit:
                node = 0
                for bit in range(29, -1, -1):
                    direction = (ordered[cursor] >> bit) & 1
                    if children[node][direction] < 0:
                        children[node][direction] = len(children)
                        children.append([-1, -1])
                    node = children[node][direction]
                cursor += 1
            if cursor:
                node = result = 0
                for bit in range(29, -1, -1):
                    direction = (value >> bit) & 1
                    if children[node][direction ^ 1] >= 0:
                        result |= 1 << bit
                        direction ^= 1
                    node = children[node][direction]
                answer[index] = result
        return answer
