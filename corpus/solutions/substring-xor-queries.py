class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        shortest = {}
        for left in range(len(s)):
            value = 0
            for right in range(left, min(len(s), left + 31)):
                value = (value << 1) | int(s[right])
                if (
                    value not in shortest
                    or right - left < shortest[value][1] - shortest[value][0]
                ):
                    shortest[value] = [left, right]
        return [shortest.get(first ^ second, [-1, -1]) for first, second in queries]
