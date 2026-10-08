from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = [i for i, x in enumerate(arr) if x]
        if not ones:
            return [0, 2]
        if len(ones) % 3:
            return [-1, -1]
        each = len(ones) // 3
        a, b, c = ones[0], ones[each], ones[2 * each]
        size = len(arr) - c
        if a + size > b or b + size > c:
            return [-1, -1]
        if arr[a : a + size] != arr[b : b + size] or arr[a : a + size] != arr[c:]:
            return [-1, -1]
        return [a + size - 1, b + size]
