class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        modulo = 10**9 + 7
        days = [0] * len(nextVisit)
        for room in range(1, len(nextVisit)):
            days[room] = (2 * days[room - 1] - days[nextVisit[room - 1]] + 2) % modulo
        return days[-1]
