class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        differences = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        operations = k1 + k2
        if sum(differences) <= operations:
            return 0
        low, high = 0, differences[0]
        while low < high:
            middle = (low + high) // 2
            needed = sum(max(0, value - middle) for value in differences)
            if needed <= operations:
                high = middle
            else:
                low = middle + 1
        level = low
        used = 0
        answer = 0
        for value in differences:
            reduced = min(value, level)
            used += value - reduced
            answer += reduced * reduced
        remaining = operations - used
        for value in differences:
            if remaining and value >= level and level > 0:
                answer -= level * level - (level - 1) * (level - 1)
                remaining -= 1
        return answer
