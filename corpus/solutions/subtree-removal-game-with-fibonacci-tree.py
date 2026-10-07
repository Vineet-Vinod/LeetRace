class Solution:
    def findGameWinner(self, n: int) -> bool:
        # A deletable rooted branch has value 1 + xor of its child branch values.
        grundy = [0, 1]
        for i in range(2, n + 1):
            grundy.append(1 + (grundy[i - 2] ^ grundy[i - 1]))
        return (grundy[n - 2] ^ grundy[n - 1]) != 0 if n > 1 else False
