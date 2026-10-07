class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo = tomatoSlices // 2 - cheeseSlices
        small = cheeseSlices - jumbo
        if tomatoSlices % 2 or jumbo < 0 or small < 0:
            return []
        return [jumbo, small]
