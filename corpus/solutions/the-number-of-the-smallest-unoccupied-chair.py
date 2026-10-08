class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        arrivals = sorted(
            (arrival, leaving, friend)
            for friend, (arrival, leaving) in enumerate(times)
        )
        occupied: list[tuple[int, int]] = []
        available: list[int] = []
        next_chair = 0
        for arrival, leaving, friend in arrivals:
            while occupied and occupied[0][0] <= arrival:
                _, chair = heappop(occupied)
                heappush(available, chair)
            chair = heappop(available) if available else next_chair
            if chair == next_chair:
                next_chair += 1
            if friend == targetFriend:
                return chair
            heappush(occupied, (leaving, chair))
        return -1
