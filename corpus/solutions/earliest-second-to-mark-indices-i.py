class Solution:
    def earliestSecondToMarkIndices(
        self, nums: List[int], changeIndices: List[int]
    ) -> int:
        n, m = len(nums), len(changeIndices)

        def feasible(seconds: int) -> bool:
            last = [-1] * n
            for time in range(seconds):
                last[changeIndices[time] - 1] = time
            if any(time < 0 for time in last):
                return False
            free = 0
            for time in range(seconds):
                index = changeIndices[time] - 1
                if last[index] == time:
                    if free < nums[index]:
                        return False
                    free -= nums[index]
                else:
                    free += 1
            return True

        low, high = 1, m
        answer = -1
        while low <= high:
            middle = (low + high) // 2
            if feasible(middle):
                answer = middle
                high = middle - 1
            else:
                low = middle + 1
        return answer
