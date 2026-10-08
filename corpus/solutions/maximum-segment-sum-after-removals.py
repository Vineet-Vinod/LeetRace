class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = list(range(n))
        sums = [0] * n
        active = [False] * n
        answer = [0] * n
        maximum = 0

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for j in range(n - 1, -1, -1):
            answer[j] = maximum
            i = removeQueries[j]
            active[i] = True
            sums[i] = nums[i]
            for other in (i - 1, i + 1):
                if 0 <= other < n and active[other]:
                    a, b = find(i), find(other)
                    parent[b] = a
                    sums[a] += sums[b]
            maximum = max(maximum, sums[find(i)])
        return answer
