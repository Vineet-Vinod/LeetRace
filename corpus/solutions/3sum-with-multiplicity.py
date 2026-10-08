class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counts = [0] * 101
        for value in arr:
            counts[value] += 1
        answer = 0
        for first in range(101):
            if counts[first] == 0:
                continue
            for second in range(first, 101):
                third = target - first - second
                if (
                    third < second
                    or third > 100
                    or counts[second] == 0
                    or counts[third] == 0
                ):
                    continue
                if first == second == third:
                    ways = (
                        counts[first] * (counts[first] - 1) * (counts[first] - 2) // 6
                    )
                elif first == second:
                    ways = counts[first] * (counts[first] - 1) // 2 * counts[third]
                elif second == third:
                    ways = counts[first] * counts[second] * (counts[second] - 1) // 2
                else:
                    ways = counts[first] * counts[second] * counts[third]
                answer += ways
        return answer % (10**9 + 7)
