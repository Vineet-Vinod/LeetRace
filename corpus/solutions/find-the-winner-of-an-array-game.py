class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        streak = 0
        for value in arr[1:]:
            if winner > value:
                streak += 1
            else:
                winner = value
                streak = 1
            if streak == k:
                return winner
        return winner
