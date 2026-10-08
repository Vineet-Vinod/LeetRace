class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remaining = Counter(nums)
        ending = defaultdict(int)
        for value in nums:
            if remaining[value] == 0:
                continue
            remaining[value] -= 1
            if ending[value - 1] > 0:
                ending[value - 1] -= 1
                ending[value] += 1
            elif remaining[value + 1] > 0 and remaining[value + 2] > 0:
                remaining[value + 1] -= 1
                remaining[value + 2] -= 1
                ending[value + 2] += 1
            else:
                return False
        return True
