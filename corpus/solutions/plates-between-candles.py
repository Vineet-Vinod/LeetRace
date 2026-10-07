class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]
        candles: list[int] = []
        for i, char in enumerate(s):
            prefix.append(prefix[-1] + (char == "*"))
            if char == "|":
                candles.append(i)
        answer: list[int] = []
        for left, right in queries:
            first = bisect_left(candles, left)
            last = bisect_right(candles, right) - 1
            if first > last:
                answer.append(0)
            else:
                answer.append(prefix[candles[last]] - prefix[candles[first]])
        return answer
