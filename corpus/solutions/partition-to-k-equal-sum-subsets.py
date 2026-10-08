class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        buckets = [0] * k

        def place(index: int) -> bool:
            if index == len(nums):
                return True
            tried: set[int] = set()
            value = nums[index]
            for bucket in range(k):
                if buckets[bucket] in tried or buckets[bucket] + value > target:
                    continue
                tried.add(buckets[bucket])
                buckets[bucket] += value
                if place(index + 1):
                    return True
                buckets[bucket] -= value
                if buckets[bucket] == 0:
                    break
            return False

        return place(0)
