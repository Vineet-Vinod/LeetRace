from bisect import bisect_right


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        values = [a - b for a, b in zip(nums1, nums2)]
        ordered = sorted(set(values))
        ranks = {x: i + 1 for i, x in enumerate(ordered)}
        bit = [0] * (len(ordered) + 1)
        answer = 0
        for x in values:
            i = bisect_right(ordered, x + diff)
            while i:
                answer += bit[i]
                i -= i & -i
            i = ranks[x]
            while i < len(bit):
                bit[i] += 1
                i += i & -i
        return answer
