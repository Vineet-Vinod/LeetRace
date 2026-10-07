class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        best_pair = [1, num + 1]
        best_gap = num
        for product in (num + 1, num + 2):
            divisor = math.isqrt(product)
            while product % divisor:
                divisor -= 1
            pair = [divisor, product // divisor]
            gap = pair[1] - pair[0]
            if gap < best_gap:
                best_gap = gap
                best_pair = pair
        return best_pair
