class Solution:
    def pathSum(self, nums: List[int]) -> int:
        values = {(x // 100, x // 10 % 10): x % 10 for x in nums}
        total = 0
        for (depth, pos), value in values.items():
            if (depth + 1, pos * 2 - 1) not in values and (
                depth + 1,
                pos * 2,
            ) not in values:
                cur = depth
                p = pos
                s = value
                while cur > 1:
                    p = (p + 1) // 2
                    cur -= 1
                    s += values[(cur, p)]
                total += s
        return total
