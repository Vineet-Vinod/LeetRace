class Solution:
    def kBigIndices(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def smaller(values: list[int]) -> list[int]:
            bit = [0] * (n + 1)
            result = []
            for value in values:
                total = 0
                j = value - 1
                while j:
                    total += bit[j]
                    j -= j & -j
                result.append(total)
                j = value
                while j <= n:
                    bit[j] += 1
                    j += j & -j
            return result

        left = smaller(nums)
        right = smaller(nums[::-1])[::-1]
        return sum(a >= k and b >= k for a, b in zip(left, right))
