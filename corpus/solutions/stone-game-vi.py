class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        order = sorted(
            range(len(aliceValues)), key=lambda i: -(aliceValues[i] + bobValues[i])
        )
        alice = bob = 0
        for turn, index in enumerate(order):
            if turn % 2 == 0:
                alice += aliceValues[index]
            else:
                bob += bobValues[index]
        return 1 if alice > bob else -1 if alice < bob else 0
