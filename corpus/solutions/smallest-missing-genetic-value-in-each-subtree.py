from __future__ import annotations
from typing import List


class Solution:
    def smallestMissingValueSubtree(
        self, parents: List[int], nums: List[int]
    ) -> List[int]:
        answer = [1] * len(nums)
        if 1 not in nums:
            return answer
        children = [[] for _ in nums]
        for i in range(1, len(nums)):
            children[parents[i]].append(i)
        node = nums.index(1)
        visited = set()
        values = set()
        missing = 1
        while node != -1:
            stack = [node]
            while stack:
                a = stack.pop()
                if a in visited:
                    continue
                visited.add(a)
                values.add(nums[a])
                stack.extend(children[a])
            while missing in values:
                missing += 1
            answer[node] = missing
            node = parents[node]
        return answer
