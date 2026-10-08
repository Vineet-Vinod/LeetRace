class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = 0
        power = 0
        while target:
            target, digit = divmod(target, x)
            if power == 0:
                pos = digit * 2
                neg = (x - digit) * 2
            else:
                pos, neg = (
                    min(digit * power + pos, (digit + 1) * power + neg),
                    min((x - digit) * power + pos, (x - digit - 1) * power + neg),
                )
            power += 1
        return min(pos, neg + power) - 1
