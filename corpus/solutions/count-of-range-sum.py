from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        def count(values: List[int]) -> tuple[int, List[int]]:
            if len(values) <= 1:
                return 0, values
            middle = len(values) // 2
            left_count, left = count(values[:middle])
            right_count, right = count(values[middle:])
            answer = left_count + right_count
            lo = hi = 0
            for value in left:
                while lo < len(right) and right[lo] - value < lower:
                    lo += 1
                while hi < len(right) and right[hi] - value <= upper:
                    hi += 1
                answer += hi - lo
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return answer, merged

        return count(prefix)[0]
