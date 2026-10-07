class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        difference = [0] * (n + 1)
        for first, last, seats in bookings:
            difference[first - 1] += seats
            difference[last] -= seats
        answer = []
        running = 0
        for value in difference[:-1]:
            running += value
            answer.append(running)
        return answer
