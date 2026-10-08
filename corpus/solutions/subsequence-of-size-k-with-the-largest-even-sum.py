class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        selected = nums[:k]
        total = sum(selected)
        if total % 2 == 0:
            return total
        smallest_odd = min((value for value in selected if value % 2), default=None)
        smallest_even = min(
            (value for value in selected if value % 2 == 0), default=None
        )
        unselected = nums[k:]
        largest_even = max(
            (value for value in unselected if value % 2 == 0), default=None
        )
        largest_odd = max((value for value in unselected if value % 2), default=None)
        options = []
        if smallest_odd is not None and largest_even is not None:
            options.append(total - smallest_odd + largest_even)
        if smallest_even is not None and largest_odd is not None:
            options.append(total - smallest_even + largest_odd)
        return max(options, default=-1)
