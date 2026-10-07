class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        answer = 0
        for house in houses:
            index = bisect_left(heaters, house)
            distance_right = (
                heaters[index] - house if index < len(heaters) else float("inf")
            )
            distance_left = house - heaters[index - 1] if index > 0 else float("inf")
            answer = max(answer, min(distance_left, distance_right))
        return answer
