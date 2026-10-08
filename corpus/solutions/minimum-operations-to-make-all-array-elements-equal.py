class Solution:
    def minOperations(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        total = prefix[-1]
        results = []
        for query in queries:
            split = bisect_left(nums, query)
            increase = query * split - prefix[split]
            decrease = total - prefix[split] - query * (len(nums) - split)
            results.append(increase + decrease)
        return results
