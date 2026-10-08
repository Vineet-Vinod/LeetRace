class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        longest = 0
        for start in range(len(nums)):
            if visited[start]:
                continue
            length = 0
            node = start
            while not visited[node]:
                visited[node] = True
                length += 1
                node = nums[node]
            longest = max(longest, length)
        return longest
