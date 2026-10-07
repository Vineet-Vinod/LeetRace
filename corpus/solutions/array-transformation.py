class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        values = arr[:]
        while True:
            nxt = values[:]
            for i in range(1, len(values) - 1):
                if values[i] < values[i - 1] and values[i] < values[i + 1]:
                    nxt[i] += 1
                elif values[i] > values[i - 1] and values[i] > values[i + 1]:
                    nxt[i] -= 1
            if nxt == values:
                return values
            values = nxt
