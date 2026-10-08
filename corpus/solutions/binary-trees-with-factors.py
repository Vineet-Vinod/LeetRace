class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        values = sorted(arr)
        ways: Dict[int, int] = {}
        present = set(values)
        for value in values:
            total = 1
            for left in values:
                if left * left > value:
                    break
                if value % left == 0:
                    right = value // left
                    if right in present:
                        total += ways[left] * ways[right] * (1 if left == right else 2)
            ways[value] = total % mod
        return sum(ways.values()) % mod
