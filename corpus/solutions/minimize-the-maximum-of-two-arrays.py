class Solution:
    def minimizeSet(
        self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int
    ) -> int:
        common = math.lcm(divisor1, divisor2)
        low, high = 1, 2 * (uniqueCnt1 + uniqueCnt2) + 1
        while low < high:
            middle = (low + high) // 2
            possible = (
                middle - middle // divisor1 >= uniqueCnt1
                and middle - middle // divisor2 >= uniqueCnt2
                and middle - middle // common >= uniqueCnt1 + uniqueCnt2
            )
            if possible:
                high = middle
            else:
                low = middle + 1
        return low
