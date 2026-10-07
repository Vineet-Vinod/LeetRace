class Solution:
    def maximumProcessableQueries(self, nums: list[int], queries: list[int]) -> int:
        n, m = len(nums), len(queries)
        dp = [0]
        answer = 0
        for length in range(n, 0, -1):
            nxt = [-1] * (n - length + 2)
            for left, processed in enumerate(dp):
                if processed == m:
                    return m
                right = left + length - 1
                take_left = processed + (nums[left] >= queries[processed])
                take_right = processed + (nums[right] >= queries[processed])
                nxt[left + 1] = max(nxt[left + 1], take_left)
                nxt[left] = max(nxt[left], take_right)
                answer = max(answer, take_left, take_right)
            dp = nxt
        return answer
