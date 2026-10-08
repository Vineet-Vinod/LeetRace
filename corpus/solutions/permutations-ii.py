class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        used = [False] * len(nums)
        path = []

        def dfs():
            if len(path) == len(nums):
                out.append(path.copy())
                return
            for i, x in enumerate(nums):
                if used[i] or (i and nums[i - 1] == x and not used[i - 1]):
                    continue
                used[i] = True
                path.append(x)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return out
