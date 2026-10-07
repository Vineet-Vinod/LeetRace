class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish = 0
        total = 0
        for arrival, duration in customers:
            finish = max(finish, arrival) + duration
            total += finish - arrival
        return total / len(customers)
