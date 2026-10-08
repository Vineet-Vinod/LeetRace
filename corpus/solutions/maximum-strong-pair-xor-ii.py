class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        answer = 0
        for shift in range(19, -1, -1):
            groups = {}
            for x in nums:
                prefix = x >> shift
                if prefix in groups:
                    low, high = groups[prefix]
                    groups[prefix] = (min(low, x), max(high, x))
                else:
                    groups[prefix] = (x, x)
            candidate = (answer << 1) | 1
            feasible = False
            for prefix, (low, high) in groups.items():
                other = prefix ^ candidate
                if other > prefix and other in groups and groups[other][0] <= 2 * high:
                    feasible = True
                    break
            answer = candidate if feasible else candidate - 1
        return answer
