class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        return sum(
            min(value, target if i <= k else target - 1)
            for i, value in enumerate(tickets)
        )
