class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        offset = len(nums) + 1
        tree = [0] * (2 * len(nums) + 5)

        def add(index: int) -> None:
            index += 1
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        def query(index: int) -> int:
            index += 1
            total = 0
            while index > 0:
                total += tree[index]
                index -= index & -index
            return total

        prefix = 0
        add(offset)
        answer = 0
        for value in nums:
            prefix += 1 if value else -1
            answer += query(offset + prefix - 1)
            add(offset + prefix)
        return answer % mod
