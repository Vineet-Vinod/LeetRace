class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = Counter()
        total = 0
        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                product = nums[first] * nums[second]
                total += products[product] * 8
                products[product] += 1
        return total
