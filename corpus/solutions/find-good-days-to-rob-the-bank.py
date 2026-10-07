class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        nonincreasing = [0] * n
        nondecreasing = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                nonincreasing[i] = nonincreasing[i - 1] + 1
            if security[i] >= security[i - 1]:
                nondecreasing[i] = nondecreasing[i - 1] + 1
        return [
            i
            for i in range(time, n - time)
            if nonincreasing[i] >= time and nondecreasing[i + time] >= time
        ]
