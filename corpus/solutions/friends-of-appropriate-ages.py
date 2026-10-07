class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1
        total = 0
        for sender in range(1, 121):
            if not counts[sender]:
                continue
            lower = sender // 2 + 7
            for receiver in range(lower + 1, sender + 1):
                total += counts[sender] * counts[receiver]
            total -= counts[sender]
        return total
