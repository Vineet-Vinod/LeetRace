class Solution:
    def nthUglyNumber(self, n: int) -> int:
        values = [1] * n
        i2 = i3 = i5 = 0
        for index in range(1, n):
            next_value = min(values[i2] * 2, values[i3] * 3, values[i5] * 5)
            values[index] = next_value
            if next_value == values[i2] * 2:
                i2 += 1
            if next_value == values[i3] * 3:
                i3 += 1
            if next_value == values[i5] * 5:
                i5 += 1
        return values[-1]
